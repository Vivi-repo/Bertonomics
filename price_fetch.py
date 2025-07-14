import yfinance as yf

def price_change(ticker="BTC-USD"):
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="2d")

        if len(hist) < 2:
            print("❌ Not enough data to compare prices.")
            return None

        latest_price = hist["Close"].iloc[-1]
        previous_price = hist["Close"].iloc[-2]
        percent_change = ((latest_price - previous_price) / previous_price) * 100
        return round(percent_change, 2)
    except Exception as e:
        print(f"❌ Could not fetch price for {ticker} → {e}")
        return None
