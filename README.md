# 📈 Autonomous AI Investment Agent

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-orange.svg)](https://deepmind.google/technologies/gemini/)

> **🥈 2nd Place Winner at Tradition Hacks '26 (Miro Canvas'26 Kolkata Chapter)**

An intent-driven financial analysis application that bridges the gap between raw market data and actionable insights. Built completely from scratch, this agent fetches real-time market metrics and generates a highly structured, data-backed investment thesis in seconds.

🔗 **Live Demo:** (https://investment-thesis-generator-shtgfymfl4vjv3faom4zas.streamlit.app/)

## ✨ Key Features

* **Real-Time Data Extraction:** Integrates with `yfinance` to instantly pull live market data, balance sheets, and key corporate financial metrics.
* **Instant Investment Thesis:** Leverages Google's Gemini 2.5 Flash to synthesize complex numbers into a clean, readable output featuring a **Bull Case**, a **Bear Case**, and a definitive **Verdict**.
* **Guarded Financial Chatbot:** Includes a context-aware follow-up chatbot embedded beneath the thesis. It is protected by strict system-level guardrails, ensuring the AI only answers finance-related queries regarding the analyzed stock and explicitly refuses off-topic questions.
* **Bring Your Own Key (BYOK) Architecture:** Features a decentralized API key input mechanism on the frontend, allowing for infinite scalability without the host incurring massive API costs, while keeping user data private.

## 🛠️ Tech Stack

* **Frontend & Backend Framework:** Streamlit (Python)
* **Market Data:** `yfinance`, `pandas`
* **Large Language Model:** Google Gemini 2.5 Flash (`google-generativeai` SDK)
* **Deployment:** Streamlit Community Cloud

## 🚀 Running the Project Locally

Follow these steps to set up the project on your local machine.

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
```

### 2. Install dependencies
Ensure you have Python installed, then run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables (Optional but recommended)
Create a `.streamlit/secrets.toml` file in the root directory to store your API key securely:
```Ini,TOML
GEMINI_API_KEY = "your_google_api_key_here"
```

### 4. Run the Streamlit app
Launch the application locally:
```Bash
streamlit run app.py
```

## 💡 How to Use
Open the web application.

* (Optional) Paste your Gemini API key in the sidebar or designated input box if you are bypassing the server's default secrets.
* Enter a valid stock ticker symbol (e.g., AAPL, TSLA, RELIANCE.NS).
* Click Generate Thesis and wait a few seconds for the AI to process the data and synthesize the report.
* Use the Chat Interface at the bottom to ask specific, finance-related follow-up questions about the generated thesis and the current stock.

## 🤝 The Team
Designed and developed collaboratively during Tradition Hacks '26 by:

* Rajarshi Sarkar

* Nirman

