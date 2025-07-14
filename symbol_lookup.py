import requests

def search_ticker(company_name):
    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={company_name}"
    try:
        response = requests.get(url)
        data = response.json()
        results = data.get("quotes", [])

        if not results:
            return None

        best = results[0]
        return {
            "symbol": best.get("symbol"),
            "shortname": best.get("shortname"),
            "exchange": best.get("exchange"),
            "quoteType": best.get("quoteType"),
        }
    except Exception as e:
        print("Ticker lookup failed:", e)
        return None
