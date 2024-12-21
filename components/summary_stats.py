import streamlit as st


def calculate_percentage_change(current_value, previous_value):
    """Calculate percentage change between two values"""
    if previous_value == 0:
        return 0
    return ((current_value - previous_value) / previous_value) * 100


def display_summary_cards(current_data, prev_data, prev_hour_data):
    """Display summary statistics in cards with percentage changes"""
    st.header("📊 Summary Statistics")

    col1, col2, col3, col4 = st.columns(4)

    # Calculate 24h price change
    price_change = calculate_percentage_change(
        current_data["open_price"], prev_data["close_price"]
    )

    # Calculate previous day's price change for delta
    prev_price_change = calculate_percentage_change(
        prev_data["open_price"],
        prev_data["close_price"],  # Replace reference to 'df' here
    )

    with col1:
        st.metric(
            "24h Price Change",
            f"${current_data['open_price']:,.2f}",
            delta=f"{price_change:.2f}%",
            delta_color="normal",
        )

    # Define metrics with their corresponding previous data type
    metrics = [
        ("Taker Buy/Sell Ratio", "taker_buy_sell_ratio", "prev_hour"),
        ("Exchange Whale Ratio", "exchange_whale_ratio", "prev_hour"),
        ("Open Interest", "open_interest", "prev_hour"),
    ]

    columns = [col2, col3, col4]

    for (label, field, prev_type), col in zip(metrics, columns):
        current_value = current_data[field]
        prev_value = (
            prev_hour_data[field] if prev_type == "prev_hour" else prev_data[field]
        )
        pct_change = calculate_percentage_change(current_value, prev_value)

        with col:
            if field == "open_interest":
                st.metric(
                    label,
                    f"{current_value:,.0f}",
                    delta=f"{pct_change:.2f}%",
                    delta_color="normal",
                )
            else:
                st.metric(
                    label,
                    f"{current_value:.2f}",
                    delta=f"{pct_change:.2f}%",
                    delta_color="normal",
                )
