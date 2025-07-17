import yfinance as yf
import ta

def analyze_technical_indicators(ticker: str):
    df = yf.download(ticker, period="6mo", interval="1d")
    close_prices = df['Close'].squeeze()
    rsi = ta.momentum.RSIIndicator(close_prices).rsi().iloc[-1]
    macd = ta.trend.MACD(close_prices).macd_diff().iloc[-1]
    signal = "Buy" if macd > 0 and rsi < 70 else "Sell" if macd < 0 and rsi > 50 else "Hold"
    return {"signal": signal, "rsi": round(rsi, 2), "macd_diff": round(macd, 4)}
if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = analyze_technical_indicators(ticker)
    print(f"Technical indicators for {ticker}:\n", result)
    print("\n📤 Final Result:\n", result)