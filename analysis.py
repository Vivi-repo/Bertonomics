from news_sentiment import average_sentiment
from price_fetch import price_change

def final_decision(sentiment_score, price_delta):
    if sentiment_score >= 0.3 and price_delta >= 0.5:
        return "✅ BUY"
    elif sentiment_score <= -0.3 and price_delta <= -0.5:
        return "❌ SELL"
    else:
        return "⏳ HOLD"

def investment_advisor(company_name, ticker, verbose=True):
    if verbose:
        print(f"Analyzing {company_name} ({ticker})...")
    score, sentiment_label = average_sentiment()
    delta = price_change(ticker)

    if delta is None:
        return {
            "sentiment": sentiment_label,
            "score": score,
            "price_delta": None,
            "decision": "❌ Could not fetch price data"
        }

    decision = final_decision(score, delta)

    return {
        "company": company_name,
        "symbol": ticker,
        "sentiment": sentiment_label,
        "score": score,
        "price_delta": delta,
        "decision": decision
    }

