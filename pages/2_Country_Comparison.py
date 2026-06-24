import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Industrial Emissions Intelligence Dashboard - Comparison", layout="wide")
st.title("Industrial Emissions Intelligence Dashboard")
st.subheader("Country Comparison")
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "clean_emissions.csv")
df = pd.read_csv(data_path)

latest_df = df[df['Year'] == 2025]

country_list = df['Country'].unique()
country_a = st.selectbox("Select Primary Country", country_list, index=0)
country_b = st.selectbox("Select Comparison Country", country_list, index=1)

comp_df = df[df['Country'].isin([country_a, country_b])]

fig = px.bar(comp_df, x="Year", y="Emissions_Mt", color="Country", barmode="group",
             title=f"Emissions Comparison: {country_a} vs {country_b}")
st.plotly_chart(fig, use_container_width=True)
