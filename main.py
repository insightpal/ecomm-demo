import pandas as pd
import numpy as np

# Create a fake sales dataset
np.random.seed(0)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Product': np.random.choice(['Laptop', 'Smartphone', 'Tablet'], size=365),
    'Quantity Sold': np.random.randint(1, 100, size=365),
    'Revenue': np.random.uniform(100, 2000, size=365)
}

sales_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
sales_df.to_csv('sales_data.csv', index=False)


import streamlit as st
import pandas as pd

# Load the fake sales dataset
sales_df = pd.read_csv('sales_data.csv')

# Create multiple tabs
st.title("E-commerce Sales Analysis")
st.subheader("Explore Sales Data")

# Add tabs to the Streamlit app
tabs = ["Overview", "Product Analysis", "Date Analysis"]
selected_tab = st.radio("Select a Tab:", tabs)

if selected_tab == "Overview":
    st.write("## Sales Overview")
    st.write(sales_df)

elif selected_tab == "Product Analysis":
    st.write("## Product Analysis")
    selected_product = st.selectbox("Select a Product:", sales_df['Product'].unique())

    product_df = sales_df[sales_df['Product'] == selected_product]
    st.write(product_df)

    # Add filters and radio buttons
    st.write("### Filter Data")
    min_quantity = st.slider("Minimum Quantity Sold", min_value=1, max_value=100, value=1)
    filtered_product_df = product_df[product_df['Quantity Sold'] >= min_quantity]
    st.write(filtered_product_df)

elif selected_tab == "Date Analysis":
    st.write("## Date Analysis")
    st.line_chart(sales_df.groupby('Date')['Revenue'].sum())

# You can add more interactions and features based on your requirements

