from __future__ import annotations
import yfinance as yf
import pandas as pd

def fetch_prices(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Descarga precios de cierre ajustados desde Yahoo Finance."""
    data = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
    df = data[["Close"]].copy()
    df.columns = ["price"]
    df.index.name = "date"
    return df

def fetch_returns(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Retornos diarios logarítmicos de un ticker."""
    df = fetch_prices(ticker, start, end)
    df["return"] = df["price"].pct_change()
    return df.dropna()
