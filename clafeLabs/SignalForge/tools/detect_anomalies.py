import yfinance as yf
import pandas as pd

def detect_anomalies(ticker: str):
    df = yf.download(ticker, period="30d", interval="1d")
    volume_mean = df['Volume'].mean().item()
    volume_today = df['Volume'].iloc[-1].item()
    if pd.notna(volume_today) and volume_today > 1.5 * volume_mean:
        return {"anomaly": "Volume Spike", "volume": int(volume_today)}
    return {"anomaly": "None"}
if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = detect_anomalies(ticker)
    print(f"Anomaly detection for {ticker}:\n", result)
    print("\n📤 Final Result:\n", result)