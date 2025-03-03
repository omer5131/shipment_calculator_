import streamlit as st

st.title("Shipment Frighet Price Calculator")

# Input fields for the four inputs
total_items_cost = st.number_input("Total Items Cost in USD", value=0.0, step=0.1, format="%.2f")
conversion_rate = st.number_input("Currenct Conversion Rate", value=0.0, step=0.1, format="%.5f")
customs_rate = st.number_input("Custom's Rate in percentiles", value=1.0, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
tax_rate = st.number_input("Tax Rate (from Israel, in percentiles)", value=1.0, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
total_taxes = st.number_input("Total Taxes in DKK", value=0.0, step=0.1, format="%.2f")

# Button to trigger the calculation
if st.button("Calculate Shipment Price"):
    # Calculate shipment price using the formula:
    # Shipment Price = ((Total Cost Include All Taxes / Custom's Rate) - Total Items Cost) / Tax Rate
    shipment_price = ((total_taxes / customs_rate) - (total_items_cost*conversion_rate)) / tax_rate
    shipment_price = round(shipment_price, 5)  # round to two decimals
    
    st.success(f"Shipment Price: {shipment_price}")
