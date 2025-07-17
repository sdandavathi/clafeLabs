import requests
from bs4 import BeautifulSoup

def get_news(ticker: str):
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    news_table = soup.find('table', class_='fullview-news-outer')
    news = []
    if news_table:
        for row in news_table.findAll('tr')[:5]:
            cols = row.findAll('td')
            news.append({"datetime": cols[0].text, "headline": cols[1].text})
    return {"headlines": news}
if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = get_news(ticker)
    print(f"News for {ticker}:\n", result['headlines'])
    print("\n📤 Final Result:\n", result)