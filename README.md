Big Data Analysis with PySpark

This project is a demonstration of a big data analysis pipeline using Python. It includes synthetic data generation, data analysis with Pandas (as a stand-in for PySpark for local development), and an interactive web dashboard for visualizing the results.

Features

Synthetic Data Generation: Creates a large dataset of synthetic sales transactions, including order ID, customer ID, product ID, price, timestamp, and store location.
Data Analysis: Performs the following analyses on the generated data:
    *   Calculates the total sales revenue per store location.
    *   Determines the top 10 best-selling products by sales count.
    *   Analyzes the monthly sales revenue trend for the most recent year.
    
Interactive Dashboard: A web-based dashboard built with Streamlit and Plotly to visualize the analysis results. The dashboard includes:
    *   Key Performance Indicators (KPIs) for total revenue and the top-performing store.
    *   Bar charts showing total revenue by store location and the top 10 best-selling products.
    *   A line chart illustrating the monthly sales trend.
    *   Expandable sections to view the raw data tables.

Technologies Used

Python: The core programming language for the project.
Pandas: Used for data manipulation and analysis. This can be swapped out for PySpark for a true big data implementation.
Streamlit: Used to create the interactive web dashboard.
Plotly: Used for creating the interactive visualizations in the dashboard.

Project Structure

```
.
├── dashboard.py
├── main.py
├── README.md
├── requirements.txt
└── results
    ├── monthly_sales.csv
    ├── revenue_by_store.csv
    └── top_products.csv
```

`main.py`: The main script that generates synthetic data and performs analysis. The results are saved in the `results` directory.
`dashboard.py`: A Streamlit application that reads the analysis results from the `results` directory and visualizes them.
`requirements.txt`: A list of Python packages required to run the project.
`results/`: A directory containing the analysis results in CSV format.

How to Run

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the main analysis script:
    ```bash
    python main.py
    ```
    This will generate the synthetic data and create the analysis result files in the `results` directory.

4.  Run the dashboard:
    ```bash
    streamlit run dashboard.py
    ```
    This will start the Streamlit web server and open the dashboard in your browser.

Dashboard Description

The dashboard provides a comprehensive overview of the sales data analysis.

Header: The dashboard is titled "Big Data Sales Analysis Dashboard".
KPIs: At the top, you'll find two key performance indicators:
Total Revenue: The total revenue from all sales.
Top Performing Store: The store with the highest total revenue.
Visualizations: The main section of the dashboard features three interactive charts:
    Total Revenue by Store Location: A bar chart that displays the total revenue for each store, allowing for a quick comparison of store performance.
    Top 10 Best-Selling Products: A horizontal bar chart that shows the top 10 products with the highest number of sales.
    Monthly Sales Trend for the Last Year: A line chart that visualizes the monthly revenue over the last year, helping to identify trends and seasonality.
*   Raw Data Tables: At the bottom of the dashboard, there are expandable sections that allow you to view the raw data for each of the analyses.

