import streamlit as st
import pandas as pd
import os

# 1. Page Configuration Setup
st.set_page_config(page_title="Industrial Emissions Intelligence Dashboard", layout="wide")

# 2. Main Locked Title Element
st.title("Industrial Emissions Intelligence Dashboard")
st.subheader("Executive Overview")

# Add a text link directly on the dashboard page
st.markdown("**Live Repository and Source Code:** [GitHub Repository](https://github.com/CodeSigma101/industrial-emissions-intelligence-dashboard)")

st.markdown("""
This platform analyzes global industrial greenhouse gas emissions trends to identify priority actions 
for industrial decarbonisation. Navigate through the sidebar to explore specific trends, sector breakdowns, 
and corporate target accountability.
""")

# 3. Secure Data Loading Pipeline
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data", "clean_emissions.csv")
df = pd.read_csv(data_path)

# 4. Global Core Metrics Calculations
total_emissions = df[df['Year'] == 2025]['Emissions_Mt'].sum()
top_emitter = df[df['Year'] == 2025].groupby('Country')['Emissions_Mt'].sum().idxmax()
top_sector = df[df['Year'] == 2025].groupby('Sector')['Emissions_Mt'].sum().idxmax()
num_countries = df['Country'].nunique()

# 5. Executive Summary KPI Display Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Global Emissions (2025)", f"{total_emissions:,} Mt CO2")
col2.metric("Top Emitter Country", top_emitter)
col3.metric("Highest Emitting Sector", top_sector)
col4.metric("Countries Monitored", num_countries)

st.info("Navigation: Use the sidebar menu to access specialized data trends, country comparison modules, and steel industry asset trackers.")
