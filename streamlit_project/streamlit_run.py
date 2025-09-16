# ---
# lambda-test: false  # auxiliary-file
# ---
# ## Demo Streamlit application.
#
# This application is the example from https://docs.streamlit.io/library/get-started/create-an-app.
#
# Streamlit is designed to run its apps as Python scripts, not functions, so we separate the Streamlit
# code into this module, away from the Modal application code.

def main():
    import numpy as np
    import pandas as pd
    import streamlit as st
    import plotly.express as px
    import altair as alt

    st.title("Uber pickups in NYC!")
    DATE_COLUMN = "date/time"
    DATA_URL = (
        "https://s3-us-west-2.amazonaws.com/"
        "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
    )

    @st.cache_data
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        data.rename(str.lower, axis="columns", inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    data_load_state = st.text("Loading data...")
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache_data)")

    if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)

    st.subheader("Number of pickups by hour")
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)

    # ---- NEW CHARTS BELOW ----
    st.subheader("Pickups by Day of Week")
    data["day_of_week"] = data[DATE_COLUMN].dt.day_name()
    day_counts = data["day_of_week"].value_counts().reset_index()
    day_counts.columns = ["day", "pickups"]

    fig1 = px.bar(day_counts, x="day", y="pickups", title="Uber Pickups by Day of Week")
    st.plotly_chart(fig1)

    st.subheader("Interactive Scatterplot of Pickups")
    x_axis = st.selectbox("Choose X-axis", options=["lat", "lon"])
    y_axis = st.selectbox("Choose Y-axis", options=["lon", "lat"])
    chart = alt.Chart(data).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color="day_of_week",
        tooltip=["date/time", "lat", "lon"]
    ).interactive()
    st.altair_chart(chart, use_container_width=True)


if __name__ == "__main__":
    main()