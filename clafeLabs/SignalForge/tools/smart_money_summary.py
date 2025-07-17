import requests
from bs4 import BeautifulSoup

def smart_money_summary(ticker: str):
    try:
        url = f"https://finviz.com/quote.ashx?t={ticker.upper()}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        insider_table = soup.find("table", class_="body-table")
        trades = []
        sentiment = "Neutral"

        if insider_table:
            rows = insider_table.find_all("tr")[1:6]  # First few insider trades
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 6:
                    trades.append({
                        "name": cols[0].text.strip(),
                        "relationship": cols[1].text.strip(),
                        "date": cols[2].text.strip(),
                        "transaction": cols[3].text.strip(),
                        "shares": cols[4].text.strip(),
                    })

            sentiment = "Bullish" if any("Buy" in t["transaction"] for t in trades) else "Bearish" if any("Sell" in t["transaction"] for t in trades) else "Neutral"

        return {
            "insider_trades": trades if trades else "No recent insider trades found",
            "sentiment": sentiment
        }

    except Exception as e:
        return {"error": str(e), "sentiment": "Neutral"}
if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = smart_money_summary(ticker)
    print(f"Smart Money Summary for {ticker}:\n", result)
    print("\n📤 Final Result:\n", result)