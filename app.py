import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from components import summary_stats, charts, trading_signals

st.set_page_config(
    page_title="Bitcoin Trading Dashboard", page_icon="📈", layout="wide"
)


# Load and process data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_um_datathon_24.csv", parse_dates=["time"])
    return df


def main():
    st.title("📊 Bitcoin Trading Dashboard")

    # Load data
    df = load_data()

    # Current Date Selection
    st.sidebar.header("📅 Current Date Selection")
    min_date = df["time"].min().date()
    max_date = df["time"].max().date()

    selected_date = st.sidebar.date_input(
        "Select Current Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )

    # Determine the maximum hour based on the selected date
    if selected_date == max_date:
        max_hour = df[df["time"].dt.date == selected_date]["time"].dt.hour.max()
    else:
        max_hour = 23

    # Convert current_datetime to datetime with hour selection
    hour = st.sidebar.slider(
        "Select Hour",
        min_value=0,
        max_value=max_hour,
        value=max_hour if selected_date == max_date else 0
    )

    # Combine selected date and hour to form current_datetime
    current_datetime = datetime.combine(
        selected_date, datetime.min.time()
    ) + timedelta(hours=hour)

    # Filter data up to current_datetime
    historical_df = df[df["time"] <= current_datetime]

    if historical_df.empty:
        st.warning("No data available for the selected date and time.")
        return

    # Get current and previous day data for summary stats
    try:
        current_data = historical_df[
            historical_df["time"].dt.date == current_datetime.date()
        ].iloc[-1]
    except IndexError:
        st.warning("No current data available for the selected date and time.")
        return

    # Calculate previous day's datetime exactly 24 hours ago
    prev_day_datetime = current_datetime - timedelta(days=1)
    try:
        prev_data = df[df["time"] == prev_day_datetime].iloc[0]
    except IndexError:
        st.warning("No previous day data available at the selected time.")
        return

    # Create prev_hour attribute
    prev_hour = current_datetime - timedelta(hours=1)
    try:
        prev_hour_data = historical_df[historical_df["time"] == prev_hour].iloc[0]
    except IndexError:
        st.warning("No previous hour data available.")
        prev_hour_data = None  # Handle accordingly in summary_stats.py

    # Display summary statistics
    summary_stats.display_summary_cards(current_data, prev_data, prev_hour_data)

    # Display charts using all historical data up to current date
    charts.display_price_volume_chart(historical_df)

    col1, col2 = st.columns(2)
    with col1:
        charts.display_coinbase_premium_chart(historical_df)
    with col2:
        charts.display_active_addresses_chart(historical_df)

    # Display trading signals
    trading_signals.display_trading_signals(historical_df)


if __name__ == "__main__":
    main()
