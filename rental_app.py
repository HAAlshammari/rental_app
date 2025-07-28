import streamlit as st
import pandas as pd
from datetime import datetime
from submit_to_sheets import submit_to_sheet  # Make sure this file is in the same folder

st.title("🏢 Rental & Investor Income Calculator")

# --- Flat Inputs ---
st.header("🏘️ Flats by Class and Rent")
col1, col2, col3 = st.columns(3)
with col1:
    flats_a = st.number_input("Number of Class A Flats", min_value=0, value=0)
    rent_a = st.number_input("Rent per Class A Flat (SAR)", min_value=0.0, value=0.0)
with col2:
    flats_b = st.number_input("Number of Class B Flats", min_value=0, value=0)
    rent_b = st.number_input("Rent per Class B Flat (SAR)", min_value=0.0, value=0.0)
with col3:
    flats_c = st.number_input("Number of Class C Flats", min_value=0, value=0)
    rent_c = st.number_input("Rent per Class C Flat (SAR)", min_value=0.0, value=0.0)

# --- Operational Cost Breakdown ---
st.header("🧾 Operational Cost Breakdown")
bill = st.number_input("Bill (SAR)", min_value=0.0, value=0.0)
cleaner = st.number_input("Cleaner (SAR)", min_value=0.0, value=0.0)
water = st.number_input("Water (SAR)", min_value=0.0, value=0.0)
operate = st.number_input("Operate (SAR)", min_value=0.0, value=0.0)
total_cost = bill + cleaner + water + operate

# --- Investor Shares ---
st.header("📊 Investor Shares (%)")
col1, col2, col3 = st.columns(3)
with col1:
    investor1 = st.number_input("Investor 1 (%)", min_value=0.0, max_value=100.0, value=34.0)
with col2:
    investor2 = st.number_input("Investor 2 (%)", min_value=0.0, max_value=100.0, value=33.0)
with col3:
    investor3 = st.number_input("Investor 3 (%)", min_value=0.0, max_value=100.0, value=33.0)

# --- Calculations ---
total_income = (flats_a * rent_a) + (flats_b * rent_b) + (flats_c * rent_c)
net_income = total_income - total_cost

if investor1 + investor2 + investor3 != 100:
    st.warning("⚠️ Investor shares must sum to 100%.")
else:
    share1 = net_income * (investor1 / 100)
    share2 = net_income * (investor2 / 100)
    share3 = net_income * (investor3 / 100)

    st.header("📈 Summary")
    st.markdown(f"**💰 Total Income:** SAR {total_income:,.2f}")
    st.markdown(f"**🧾 Total Operational Cost:** SAR {total_cost:,.2f}")
    st.markdown(f"**📉 Net Income (After Cost):** SAR {net_income:,.2f}")

    st.subheader("Investor Net Income (After Cost)")
    st.success(f"Investor 1: SAR {share1:,.2f}")
    st.success(f"Investor 2: SAR {share2:,.2f}")
    st.success(f"Investor 3: SAR {share3:,.2f}")

    # --- Export Summary Table for Review ---
    now = datetime.now().strftime("%Y-%m-%d")
    export_data = {
        "Date": [now],
        "Flats_A": [flats_a],
        "Flats_B": [flats_b],
        "Flats_C": [flats_c],
        "Total_Operational_Cost": [round(total_cost, 2)],
        "Total_Income": [round(total_income, 2)],
        "Investor1_Net_Income": [round(share1, 2)],
        "Investor2_Net_Income": [round(share2, 2)],
        "Investor3_Net_Income": [round(share3, 2)],
    }
    df = pd.DataFrame(export_data)
    st.dataframe(df)

    # --- Submit Button ---
    if st.button("📤 Submit to Google Sheet"):
        try:
            submit_to_sheet(
                now,
                flats_a,
                flats_b,
                flats_c,
                round(total_cost, 2),
                round(total_income, 2),
                round(share1, 2),
                round(share2, 2),
                round(share3, 2)
            )
            st.success("✅ Data successfully submitted to Google Sheet.")
        except Exception as e:
            st.error(f"❌ Submission failed: {e}")
