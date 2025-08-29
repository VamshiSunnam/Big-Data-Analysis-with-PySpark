import random
import uuid
from datetime import datetime, timedelta
import pandas as pd
import os

def generate_synthetic_data(num_rows):
    """Generates synthetic sales transaction data."""
    store_locations = ["New York", "London", "Tokyo", "Paris", "Singapore", "Sydney", "Dubai", "Hong Kong", "Shanghai", "Los Angeles"]
    data = []
    for _ in range(num_rows):
        data.append({
            "order_id": str(uuid.uuid4()),
            "customer_id": str(uuid.uuid4()),
            "product_id": f"prod_{random.randint(1, 100)}",
            "price": round(random.uniform(10.0, 500.0), 2),
            "timestamp": datetime.now() - timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59)),
            "store_location": random.choice(store_locations)
        })
    return data

def main():
    """Generates data, performs analysis with pandas, and saves results."""
    # Generate synthetic data
    num_rows = 1_000_000
    print(f"Generating {num_rows} synthetic sales transactions...")
    synthetic_data = generate_synthetic_data(num_rows)

    # Create a pandas DataFrame
    print("Loading data into pandas DataFrame...")
    sales_df = pd.DataFrame(synthetic_data)

    # Create the results directory if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')

    # Analysis 1: Total sales revenue per store location
    print("Analyzing revenue by store...")
    revenue_by_store = sales_df.groupby('store_location')['price'].sum().reset_index()
    revenue_by_store.rename(columns={'price': 'total_revenue'}, inplace=True)
    revenue_by_store = revenue_by_store.sort_values(by='total_revenue', ascending=False)
    revenue_by_store.to_csv("results/revenue_by_store.csv", index=False)
    print("Saved revenue_by_store.csv")

    # Analysis 2: Top 10 best-selling products by sales count
    print("Analyzing top products...")
    top_products = sales_df['product_id'].value_counts().nlargest(10).reset_index()
    top_products.columns = ['product_id', 'sales_count']
    top_products.to_csv("results/top_products.csv", index=False)
    print("Saved top_products.csv")

    # Analysis 3: Monthly sales revenue trend for the most recent year
    print("Analyzing monthly sales trend...")
    sales_df['sale_year'] = sales_df['timestamp'].dt.year
    sales_df['sale_month'] = sales_df['timestamp'].dt.month
    most_recent_year = sales_df['sale_year'].max()
    monthly_revenue = sales_df[sales_df['sale_year'] == most_recent_year].groupby(['sale_year', 'sale_month'])['price'].sum().reset_index()
    monthly_revenue.rename(columns={'price': 'monthly_revenue'}, inplace=True)
    monthly_revenue = monthly_revenue.sort_values(by='sale_month')
    monthly_revenue.to_csv("results/monthly_sales.csv", index=False)
    print("Saved monthly_sales.csv")

    print("\nSuccessfully generated all result files.")

if __name__ == "__main__":
    main()
