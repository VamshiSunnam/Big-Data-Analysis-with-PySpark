# dashboard.py
# An interactive web dashboard to visualize PySpark analysis results.

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Big Data Sales Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load Data ---
@st.cache_data
def load_data(file_path):
    """Loads a CSV file into a Pandas DataFrame with lowercase column names."""
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.lower()  # normalize column names
        return df
    except FileNotFoundError:
        st.error(f"Error: The file {file_path} was not found. Please run the main.py script first to generate the results.")
        return None

df_revenue = load_data("results/revenue_by_store.csv")
df_products = load_data("results/top_products.csv")
df_monthly = load_data("results/monthly_sales.csv")

# --- Dashboard Interface ---
st.title("📊 Big Data Sales Analysis Dashboard")
st.markdown("This dashboard visualizes the results of a large-scale sales data analysis performed with PySpark.")

# --- Main Content ---
if df_revenue is not None and df_products is not None and df_monthly is not None:
    # --- Key Metrics ---
    total_revenue = df_revenue['total_revenue'].sum()
    top_store = df_revenue.loc[df_revenue['total_revenue'].idxmax()]
    
    st.header("Key Performance Indicators (KPIs)")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
    with col2:
        st.metric(label="Top Performing Store", value=f"{top_store['store_location']} (${top_store['total_revenue']:,.2f})")

    st.markdown("---")

    # --- Visualizations ---
    st.header("Visual Analysis")
    
    col1, col2 = st.columns(2)

    with col1:
        # 1. Total Revenue by Store Location
        st.subheader("Total Revenue by Store Location")
        fig_revenue = px.bar(
            df_revenue, 
            x='store_location', 
            y='total_revenue',
            title="Store Performance",
            color='store_location',
            labels={'store_location': 'Store Location', 'total_revenue': 'Total Revenue ($)'}
        )
        st.plotly_chart(fig_revenue, use_container_width=True)

    with col2:
        # 2. Top 10 Best-Selling Products
        st.subheader("Top 10 Best-Selling Products")
        fig_products = px.bar(
            df_products, 
            x='sales_count', 
            y='product_id',
            orientation='h',
            title="Product Sales Volume",
            color='product_id',
            labels={'product_id': 'Product ID', 'sales_count': 'Number of Sales'}
        ).update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig_products, use_container_width=True)

    # 3. Monthly Sales Trend
    st.subheader("Monthly Sales Trend for the Last Year")
    df_monthly['date'] = pd.to_datetime(
        df_monthly['sale_year'].astype(str) + '-' + df_monthly['sale_month'].astype(str),
        errors='coerce'
    )
    fig_monthly = px.line(
        df_monthly, 
        x='date', 
        y='monthly_revenue',
        title="Revenue Over Time",
        markers=True,
        labels={'date': 'Month', 'monthly_revenue': 'Monthly Revenue ($)'}
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

    # --- Raw Data Tables ---
    st.markdown("---")
    st.header("Raw Data Tables")
    
    with st.expander("Revenue by Store Data"):
        st.dataframe(df_revenue)
    
    with st.expander("Top Products Data"):
        st.dataframe(df_products)
    
    with st.expander("Monthly Sales Data"):
        st.dataframe(df_monthly)

else:
    st.warning("Could not load data. Please ensure the `main.py` script has been run successfully.")
