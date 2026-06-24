import streamlit as st
import pandas as pd

st.set_page_config(page_title="Industrial Emissions Intelligence Dashboard - Steel Focus", layout="wide")
st.title("Industrial Emissions Intelligence Dashboard")
st.subheader("Steel Industry Focus")

import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "steel_tracker.csv")
tracker_df = pd.read_csv(data_path)


search_query = st.text_input("Search Steel Producer:", "")
status_filter = st.selectbox("Filter by Action Status:", ["All"] + list(tracker_df['Status'].unique()))

processed_df = tracker_df.copy()
if search_query:
    processed_df = processed_df[processed_df['Company'].str.contains(search_query, case=False)]
if status_filter != "All":
    processed_df = processed_df[processed_df['Status'] == status_filter]

st.dataframe(processed_df, use_container_width=True)
