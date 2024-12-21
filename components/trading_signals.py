import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def display_trading_signals(df):
    """Display trading signals section"""
    st.header("🎯 Trading Signals")

    # Calculate signals using utility function
    df_signals = df.copy()

    fig = go.Figure()

    # Add price line
    fig.add_trace(
        go.Scatter(
            x=df_signals["time"],
            y=df_signals["close_price"],
            name="Price",
            line=dict(color="#2962FF"),
        )
    )

    # Add buy signals
    buy_signals = df_signals[df_signals["signal"] == 1]
    fig.add_trace(
        go.Scatter(
            x=buy_signals["time"],
            y=buy_signals["close_price"],
            name="Buy Signal",
            mode="markers",
            marker=dict(symbol="triangle-up", size=15, color="#00C853"),
        )
    )

    # Add sell signals
    sell_signals = df_signals[df_signals["signal"] == -1]
    fig.add_trace(
        go.Scatter(
            x=sell_signals["time"],
            y=sell_signals["close_price"],
            name="Sell Signal",
            mode="markers",
            marker=dict(symbol="triangle-down", size=15, color="#FF3D00"),
        )
    )

    fig.update_layout(
        title="Trading Signals", xaxis_title="Date", yaxis_title="Price", height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # Display indicators table
    st.subheader("📊 Key Indicators")

    indicators_df = df_signals[
        ["time", "exchange_whale_ratio", "taker_buy_sell_ratio", "open_interest"]
    ].tail(10)
    st.dataframe(indicators_df)

    # Display indicator explanations
    st.subheader("📝 Indicator Explanations")

    st.markdown(
        """
    - **Exchange Whale Ratio**: Measures the proportion of large transactions on exchanges. High values may indicate potential selling pressure from large holders.
    - **Taker Buy/Sell Ratio**: Compares aggressive buying vs. selling pressure. Values > 1 indicate stronger buying pressure.
    - **Open Interest**: Total value of outstanding derivative contracts. Increasing values suggest growing market participation.
    """
    )
