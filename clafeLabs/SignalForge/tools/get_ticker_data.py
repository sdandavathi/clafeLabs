import yfinance as yf

def get_ticker_data(ticker: str):
    df = yf.download(ticker, period="6mo", interval="1d")
    return {"ohlc": df.tail(30).to_dict(orient="records")}
if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = get_ticker_data(ticker)
    print(f"OHLC data for {ticker}:\n", result['ohlc'])
    print("\n📤 Final Result:\n", result)