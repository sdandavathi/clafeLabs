import matplotlib.pyplot as plt
import yfinance as yf
from io import BytesIO
import base64
import os
from datetime import datetime

def plot_price_chart_with_signals(ticker, signals=None, output_dir="reports"):
    """
    signals: List of dicts with format:
      [{"date": "2024-06-01", "type": "buy"}, {"date": "2024-07-01", "type": "sell"}]
    """
    data = yf.download(ticker, period="3mo", interval="1d")
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, data["Close"], label="Close Price", linewidth=2)

    if signals:
        for signal in signals:
            date = signal["date"]
            if date in data.index.strftime("%Y-%m-%d"):
                price = data.loc[data.index.strftime("%Y-%m-%d") == date]["Close"].values[0]
                color = "green" if signal["type"] == "buy" else "red"
                marker = "^" if signal["type"] == "buy" else "v"
                label = f"{signal['type'].capitalize()} Signal"
                plt.plot(date, price, marker=marker, color=color, markersize=10, label=label)

    plt.title(f"{ticker} Price - Last 3 Months with Signals")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()

    # Save to buffer for base64
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")

    # Save to local file
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    local_path = os.path.join(output_dir, f"{ticker}_chart_{timestamp}.png")
    plt.savefig(local_path)

    plt.close()
    return encoded