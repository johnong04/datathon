import pandas as pd
import numpy as np


def calculate_price_change(df):
    """Calculate 24h price change percentage"""
    df["price_change_24h"] = df["close_price"].pct_change(24) * 100
    return df["price_change_24h"].iloc[-1]


def calculate_moving_averages(df):
    """Calculate various moving averages for technical analysis"""
    df["MA7"] = df["close_price"].rolling(window=7).mean()
    df["MA25"] = df["close_price"].rolling(window=25).mean()
    return df


def generate_trading_signals(df):
    """Generate trading signals based on multiple indicators"""
    signals = []

    # Example signal generation logic
    df["signal"] = 0

    # Bullish conditions
    bullish = (
        (df["taker_buy_sell_ratio"] > 1.2)  # Strong buying pressure
        & (df["exchange_whale_ratio"] < 0.85)  # Whales not dumping
        & (df["open_interest"].pct_change() > 0)  # Increasing open interest
    )

    # Bearish conditions
    bearish = (
        (df["taker_buy_sell_ratio"] < 0.8)  # Strong selling pressure
        & (df["exchange_whale_ratio"] > 1.15)  # Whales potentially dumping
        & (df["open_interest"].pct_change() < 0)  # Decreasing open interest
    )

    df.loc[bullish, "signal"] = 1  # Buy signal
    df.loc[bearish, "signal"] = -1  # Sell signal

    return df
