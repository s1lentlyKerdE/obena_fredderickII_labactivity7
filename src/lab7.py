# lab7.py
import pandas as pd
import plotly.express as px
import os   

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

# === Step 1: Load Dataset ===
df = pd.read_csv("data/uboats.csv")

print("Dataset loaded successfully!")
print(df.head())
print(df.info())

# === Step 2: Test Case 1 - Merchant Ships Sunk per Year ===
merchant_per_year = df.groupby("Year")["Merchant_Ships_sunk_No"].sum().reset_index()

fig1 = px.bar(
    merchant_per_year,
    x="Year",
    y="Merchant_Ships_sunk_No",
    title="Merchant Ships Sunk per Year"
)
fig1.write_image("screenshots/test_case1.png")   # save chart
fig1.show()

# === Step 3: Test Case 2 - Warships Sunk (1942–1945) ===
df_subset = df[(df["Year"] >= 1942) & (df["Year"] <= 1945)]
warships_per_year = df_subset.groupby("Year")["Warships_sunk_n_total_loss_No"].sum().reset_index()

fig2 = px.line(
    warships_per_year,
    x="Year",
    y="Warships_sunk_n_total_loss_No",
    title="Warships Sunk (1942–1945)"
)
fig2.write_image("screenshots/test_case2.png")
fig2.show()

# === Step 4: Test Case 3 - Patrols vs Merchant Ships Sunk ===
fig3 = px.scatter(
    df,
    x="Patrols_Count",
    y="Merchant_Ships_sunk_No",
    title="Patrols vs Merchant Ships Sunk",
    hover_data=["Name", "Year"]
)
fig3.write_image("screenshots/test_case3.png")
fig3.show()

print("All test cases executed. Charts saved in screenshots/ folder.")
