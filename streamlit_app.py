import streamlit as st

# Set the page configuration (optional)
st.set_page_config(
    page_title="Shipment Price Calculator", 
    page_icon="https://www.ilcargo.com/wp-content/uploads/2024/03/logo.svg",
    layout="wide"
)

# Define your logo URL
logo_url = "https://www.ilcargo.com/wp-content/uploads/2024/03/logo.svg"

# Create columns: left column for logo, right column for title
col1, col2 = st.columns([1, 5])  # adjust ratio as you like

with col1:
    st.image(logo_url, width=80)  # adjust width as needed

with col2:
    st.title("Shipment Freight Price Calculator")



# Input fields for the four inputs
total_items_cost = st.number_input("Total Items Cost in USD", value=0.0, step=0.1, format="%.2f")
conversion_rate = st.number_input("Currenct Conversion Rate", value=0.0, step=0.1, format="%.5f")
customs_rate = st.number_input("Custom % duty ", value=0.12, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
tax_rate = st.number_input(" Freight Percentage (from Israel, in percentiles)", value=0.27, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
total_taxes = st.number_input("Total Taxes in DKK", value=0.0, step=0.1, format="%.2f")

# Button to trigger the calculation
if st.button("Calculate Freight Cost"):
    # Calculate shipment price using the formula:
    # Shipment Price = ((Total Cost Include All Taxes / Custom's Rate) - Total Items Cost) / Tax Rate
    shipment_price = ((total_taxes / customs_rate) - (total_items_cost*conversion_rate)) / tax_rate
    shipment_price = round(shipment_price, 5)  # round to two decimals
    
    st.success(f"Freight Cost : {shipment_price}")
