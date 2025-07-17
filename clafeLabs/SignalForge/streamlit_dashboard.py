import streamlit as st
from ai_workflow import run_stock_workflow

st.set_page_config(page_title="Buy/Sell Signal Generator", layout="wide")
st.title("📈 AI Workflow: Stock Buy/Sell Signal Generator")

ticker = st.text_input("Enter ticker symbol (e.g., AAPL, TSLA)", value="AAPL")

if st.button("Get Signal"):
    with st.spinner("Running AI Workflow..."):
        result = run_stock_workflow(ticker)
        st.markdown("## 🧠 Signal Summary")
        st.markdown(result)