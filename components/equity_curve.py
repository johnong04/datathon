import os
import streamlit as st
from PIL import Image


def display_trading_statistics():
    """Display trading statistics in a formatted way"""
    stats = {
        "Total Return": "15.90%",
        "Sharpe Ratio (Annualized)": "0.22",
        "Max Drawdown": "-1.33%",
        "Win Rate": "22.50%",
        "Total Number of Trades": "3,363",
        "Total Trading Fees": "67.2600",
        "Trading Period (hours)": "8,170",
        "Trades per Hour": "0.4116",
        "Profit Factor": "1.03",
    }

    return stats


def display_equity_curve_section():
    """Display equity curve and trading statistics"""
    st.header("📈 Equity Curve & Trading Statistics")

    col1, col2 = st.columns([0.6, 0.4])

    with col1:
        st.subheader("Equity Curve")

        # Load equity curve image
        image = Image.open(os.path.join("images", "equity_curve.jpg"))
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("Trading Statistics")

        stats = display_trading_statistics()

        # Create a clean layout for statistics
        for metric, value in stats.items():
            st.markdown(
                f"""
                <div style='
                    padding: 10px;
                    margin: 5px 0;
                    background-color: #f0f2f6;
                    border-radius: 5px;
                '>
                    <span style='color: #666;'>{metric}:</span>
                    <span style='float: right; font-weight: bold;'>{value}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
