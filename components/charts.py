import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


def display_price_volume_chart(df):
    """Display price and volume chart"""
    st.header("💹 Price & Volume")

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add price line
    fig.add_trace(
        go.Scatter(
            x=df["time"], y=df["close_price"], name="Price", line=dict(color="#2962FF")
        ),
        secondary_y=False,
    )

    # Add volume bars
    fig.add_trace(
        go.Bar(
            x=df["time"],
            y=df["volume"],
            name="Volume",
            marker_color="rgba(41, 98, 255, 0.3)",
        ),
        secondary_y=True,
    )

    fig.update_layout(title="Bitcoin Price and Volume", xaxis_title="Date", height=500)

    st.plotly_chart(fig, use_container_width=True)


def display_coinbase_premium_chart(df):
    """Display Coinbase Premium Index chart"""
    st.subheader("📈 Coinbase Premium Index")

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["coinbase_premium_index"],
            name="Premium Index",
            line=dict(color="#00C853"),
        )
    )

    fig.update_layout(xaxis_title="Date", yaxis_title="Premium Index", height=400)

    st.plotly_chart(fig, use_container_width=True)


def display_active_addresses_chart(df):
    """Display Active Addresses chart"""
    st.subheader("👥 Active Addresses")

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["time"],
            y=df["addresses_count_active"],
            name="Active Addresses",
            line=dict(color="#FF6D00"),
        )
    )

    fig.update_layout(xaxis_title="Date", yaxis_title="Active Addresses", height=400)

    st.plotly_chart(fig, use_container_width=True)
