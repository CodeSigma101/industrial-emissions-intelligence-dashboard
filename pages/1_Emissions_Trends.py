import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Industrial Emissions Intelligence Dashboard - Trends", layout="wide")
st.title("Industrial Emissions Intelligence Dashboard")
st.subheader("Emissions Trends")

import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "clean_emissions.csv")
df = pd.read_csv(data_path)


sectors = st.multiselect("Filter by Sector", options=df['Sector'].unique(), default=df['Sector'].unique())
filtered_df = df[df['Sector'].isin(sectors)]

trend_data = filtered_df.groupby(['Year', 'Country'])['Emissions_Mt'].sum().reset_index()
fig = px.line(trend_data, x="Year", y="Emissions_Mt", color="Country", markers=True,
              title="Emissions Trajectory Over Time (Mt CO2)")
st.plotly_chart(fig, use_container_width=True)
