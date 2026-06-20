import streamlit as st
import yfinance as yf
from google import genai
import pandas as pd
import os
# Ensure clean layout
st.set_page_config(page_title="Investment Thesis Generator", page_icon="📈", layout="wide")
# Custom CSS for minimal aesthetics
st.markdown("""
<style>
    div[data-testid="stSidebarHeader"] {display: none;}
    .main {background-color: #0e1117;}
    h1 {font-weight: 300;}
</style>
""", unsafe_allow_html=True)
st.title("📈 High-Growth Investment Thesis Generator")
st.markdown("Enter a stock ticker to extract financial data and generate an AI-powered investment thesis evaluating its high-growth potential.")
# Sidebar for inputs
with st.sidebar:
    st.header("Configuration")
    ticker_input = st.text_input("Stock Ticker", value="NVDA").upper()
    api_key = st.text_input("Gemini API Key", type="password", help="Enter your Gemini API key here or set GEMINI_API_KEY as an env variable.")
    generate_btn = st.button("Generate Thesis", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.caption("This app uses yfinance to fetch market data and the Gemini API to construct the thesis.")
def fetch_stock_data(ticker):
    """Fetches P/E ratio, revenue growth, and 12-mo historical data."""
    stock = yf.Ticker(ticker)
    
    # Get basic info
    info = stock.info
    trailing_pe = info.get("trailingPE", "N/A")
    revenue_growth = info.get("revenueGrowth", "N/A")
    
    # Format revenue growth if available
    if revenue_growth != "N/A" and revenue_growth is not None:
        revenue_growth = f"{revenue_growth * 100:.2f}%"
        
    # Get 12 months historical data
    hist = stock.history(period="1y")
    
    if hist.empty:
        return None, None, None
        
    return trailing_pe, revenue_growth, hist
def generate_thesis(api_key, ticker, trailing_pe, revenue_growth, hist_data):
    """Calls Gemini API to generate the thesis."""
    # Format recent history to save tokens
    # Grouping by month end, taking the last close price
    recent_hist = hist_data[['Close', 'Volume']].resample('ME').last().tail(12)
    hist_str = recent_hist.to_string()
    
    prompt = f"""You are a professional financial analyst. Evaluate the high-growth potential of {ticker}.
Financial data for {ticker}:
- Trailing P/E Ratio: {trailing_pe}
- Revenue Growth: {revenue_growth}
Last 12 months end-of-month price and volume data:
{hist_str}
STRICT FORMATTING RULES — you must follow these exactly:
1. Do NOT write large paragraphs. Every point must be a concise bullet point.
2. Structure your response using exactly these three markdown H3 headers, in this order:
   ### The Bull Case
   ### The Bear Case
   ### The Verdict
3. Under each header, use 3-5 bullet points. Each bullet must be one or two sentences maximum.
4. Focus on the growth narrative, market opportunity, and whether the P/E and revenue growth justify growth expectations.
5. Do NOT add any text before the first header or after the last bullet point.
"""
    
    client = genai.Client(api_key=api_key)
    models_to_try = ['gemini-3.0-flash', 'gemini-2.5-flash']
    last_error = None
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            last_error = e
            continue
    raise last_error
if generate_btn:
    if not ticker_input:
        st.error("Please enter a valid ticker.")
    else:
        # Determine API key
        final_api_key = api_key if api_key else os.environ.get("GEMINI_API_KEY")
        if not final_api_key:
            st.error("Gemini API key is required. Please enter it in the sidebar or set the GEMINI_API_KEY environment variable.")
        else:
            with st.spinner(f"Fetching data for {ticker_input}..."):
                try:
                    pe, rev_growth, hist = fetch_stock_data(ticker_input)
                    if hist is None:
                        st.error(f"Could not fetch data for ticker {ticker_input}. Please check the ticker symbol.")
                        st.stop()
                except Exception as e:
                    st.error(f"Error fetching stock data: {e}")
                    st.stop()
                    
            # Layout for data display
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Ticker", ticker_input)
            with col2:
                st.metric("Trailing P/E", pe)
            with col3:
                st.metric("Revenue Growth", rev_growth)
                
            # Chart
            st.subheader("12-Month Price History")
            st.line_chart(hist['Close'], color="#8c52ff")
            
            with st.spinner("Generating Investment Thesis with Gemini..."):
                try:
                    thesis = generate_thesis(final_api_key, ticker_input, pe, rev_growth, hist)
                    st.subheader("Investment Thesis")
                    st.write(thesis)
                except Exception as e:
                    st.error(f"Error generating thesis: {e}")
