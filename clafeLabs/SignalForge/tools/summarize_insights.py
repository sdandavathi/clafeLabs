import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_insights(ticker: str, **kwargs):
    prompt = f"""
You are a stock analyst. Below is the output from various analysis tools for the stock {ticker}:

"""
    for tool_name, result in kwargs.items():
        prompt += f"### {tool_name} output:\n{result}\n\n"

    prompt += f"""
Based on the above data including technical indicators, sentiment, smart money flow, anomalies, and macro conditions,
give a final decision to Buy, Sell, or Hold the stock {ticker}. Explain your reasoning in 1-2 lines and give a confidence score out of 100.

Respond in JSON format like: {{"signal": "Buy", "confidence": 92, "reason": "..."}}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return eval(response.choices[0].message.content.strip())

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = summarize_insights(ticker)
    print(f"Final insights for {ticker}:\n", result)
    print("\n📤 Final Result:\n", result)