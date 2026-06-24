import os

# Create the data directory if it does not exist
os.makedirs("data", exist_ok=True)

# Write the emissions dataset
clean_emissions_data = """Year,Country,Region,Sector,Emissions_Mt
2020,China,Asia,Steel,1200
2025,China,Asia,Steel,1350
2020,China,Asia,Cement,850
2025,China,Asia,Cement,900
2020,Germany,Europe,Steel,45
2025,Germany,Europe,Steel,38
2020,Germany,Europe,Energy,120
2025,Germany,Europe,Energy,95
2020,United States,Americas,Energy,1500
2025,United States,Americas,Energy,1380
2020,United States,Americas,Steel,80
2025,United States,Americas,Steel,72
2020,South Africa,Africa,Steel,18
2025,South Africa,Africa,Steel,19"""

with open(os.path.join("data", "clean_emissions.csv"), "w") as f:
    f.write(clean_emissions_data)

# Write the steel tracker dataset
steel_tracker_data = """Company,Country,Production_Capacity,Emissions_Trend,Status,SBTi_Status
Ansteel Group,China,Very High,Increasing,Needs Action,Committed
ArcelorMittal,Luxembourg,High,Improving,Transitioning,Approved
Nippon Steel,Japan,High,Stable,Needs Action,No Target
Nucor Corporation,United States,Medium,Improving,Transitioning,Approved
SSAB,Sweden,Low,Improving,Transitioning,Approved
POSCO,South Korea,High,Stable,Needs Action,Committed"""

with open(os.path.join("data", "steel_tracker.csv"), "w") as f:
    f.write(steel_tracker_data)

print("Data folder and CSV files generated successfully!")
