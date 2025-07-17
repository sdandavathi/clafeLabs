import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(ticker: str):
    prompt = f"Analyze sentiment for recent news on {ticker}. Return positive, neutral, or negative with reason."

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"sentiment": response.choices[0].message.content.strip()}

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = analyze_sentiment(ticker)
    print(f"Sentiment for {ticker}: {result['sentiment']}")
    print("\n📤 Final Result:\n", result)