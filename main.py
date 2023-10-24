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
import numpy as np
import altair as alt

# Load the fake sales dataset
sales_df = pd.read_csv('sales_data.csv')

# Add tabs to the Streamlit app
st.title("E-commerce Sales Analysis")
st.subheader("Explore Sales Data")

# Create multiple tabs using st.submenu
tabs = st.radio("Select a Tab:", ("Overview", "Product Analysis", "Date Analysis", "Data Visualization"))

if tabs == "Overview":
    st.write("## Sales Overview")
    st.dataframe(sales_df)

elif tabs == "Product Analysis":
    st.write("## Product Analysis")
    selected_product = st.selectbox("Select a Product:", sales_df['Product'].unique())

    product_df = sales_df[sales_df['Product'] == selected_product]

    # Add filters and radio buttons
    st.write("### Filter Data")
    min_quantity = st.slider("Minimum Quantity Sold", min_value=1, max_value=100, value=1)
    filtered_product_df = product_df[product_df['Quantity Sold'] >= min_quantity]
    st.dataframe(filtered_product_df)

elif tabs == "Date Analysis":
    st.write("## Date Analysis")
    st.line_chart(sales_df.groupby('Date')['Revenue'].sum())

elif tabs == "Data Visualization":
    st.write("## Data Visualization")

    # Interactive Scatter Plot
    st.write("### Interactive Scatter Plot")
    selected_metric = st.selectbox("Select a Metric:", ('Quantity Sold', 'Revenue'))
    c = alt.Chart(sales_df).mark_circle().encode(
        x='Date',
        y=selected_metric,
        color='Product',
        size='Quantity Sold'
    ).interactive()
    st.altair_chart(c, use_container_width=True)

    # Distribution Plot
    st.write("### Distribution Plot")
    selected_feature = st.selectbox("Select a Feature:", ('Quantity Sold', 'Revenue'))
    hist_values = np.histogram(sales_df[selected_feature], bins=20)[0]
    st.bar_chart(hist_values)

    # Advanced filters
    st.write("### Advanced Filters")
    min_revenue = st.number_input("Minimum Revenue", value=0, min_value=0, max_value=int(sales_df['Revenue'].max()))
    filtered_data = sales_df[sales_df['Revenue'] >= min_revenue]
    st.dataframe(filtered_data)


