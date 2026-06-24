import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Industrial Emissions Intelligence Dashboard - Sectors", layout="wide")
st.title("Industrial Emissions Intelligence Dashboard")
st.subheader("Industrial Sector Analysis")

import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "clean_emissions.csv")
df = pd.read_csv(data_path)

latest_df = df[df['Year'] == 2025]

sector_df = latest_df.groupby('Sector')['Emissions_Mt'].sum().reset_index().sort_values(by="Emissions_Mt", ascending=True)
fig = px.bar(sector_df, x="Emissions_Mt", y="Sector", orientation='h', 
             title="Emissions Burden by Industrial Sector (2025)",
             color="Emissions_Mt", color_continuous_scale="Reds")
st.plotly_chart(fig, use_container_width=True)
