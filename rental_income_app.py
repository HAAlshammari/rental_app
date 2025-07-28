import streamlit as st
from datetime import date
from submit_form import submit_to_google_form

st.title("Rental Income Submission")

date_selected = st.date_input("Date", value=date.today())
num_flats = st.number_input("Number of Flats", min_value=0)
rent_per_flat = st.number_input("Rent per Flat", min_value=0.0)
num_stores = st.number_input("Number of Stores", min_value=0)
rent_per_store = st.number_input("Rent per Store", min_value=0.0)
operation_cost = st.number_input("Operational Cost", min_value=0.0)

st.subheader("Investor Shares")
meshal_share = st.slider("Meshal %", 0, 100, 34)
hamed_share = st.slider("Hamed %", 0, 100, 33)
mohammad_share = st.slider("Mohammad %", 0, 100, 33)

if meshal_share + hamed_share + mohammad_share != 100:
    st.warning("Total share must equal 100%")
else:
    if st.button("Submit to Google Form"):
        try:
            submit_to_google_form(
                date_selected.strftime("%Y-%m-%d"),
                num_flats,
                rent_per_flat,
                num_stores,
                rent_per_store,
                operation_cost,
                meshal_share,
                hamed_share,
                mohammad_share,
            )
            st.success("Submitted successfully.")
        except Exception as e:
            st.error(f"Failed to submit: {e}")
