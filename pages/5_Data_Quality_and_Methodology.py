import streamlit as st

st.set_page_config(page_title="Industrial Emissions Intelligence Dashboard - Methodology", layout="wide")
st.title("Industrial Emissions Intelligence Dashboard")
st.subheader("Data Quality and Methodology")

st.markdown("""
### Data Provenance
Data ingested into this tracker is synthesized from public corporate disclosures, sustainability annual indexes, and verified open-source climate registries.

### Analytical Adjustments and Cleaning
* **Missing Value Allocation:** Imputed data arrays utilize multi-year rolling industry averages.
* **Scope Definition:** Emissions explicitly measure Scope 1 (Direct manufacturing) and Scope 2 (Purchased electricity dependencies) footprints to maintain analytical consistency.
* **Data Refresh Cadence:** Updated bi-annually following annual public report drops.
""")
