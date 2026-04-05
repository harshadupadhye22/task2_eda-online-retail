import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
if not os.path.exists("eda_output"):
    os.makedirs("eda_output")

# Load dataset
df = pd.read_csv("cleaned_online_retail.csv")

print("Dataset Loaded")

# -------------------------------
# 1. SUMMARY STATISTICS
# -------------------------------
summary = df.describe()
summary.to_csv("eda_output/summary_statistics.csv")

# -------------------------------
# 2. BUSINESS ANALYSIS
# -------------------------------

# Top 5 Sub-Categories
top_products = df.groupby('Sub Category')['Total Sales'].sum().sort_values(ascending=False).head(5)
top_products.to_csv("eda_output/top_products.csv")

# Sales by Category
category_sales = df.groupby('Category')['Total Sales'].sum()
category_sales.to_csv("eda_output/category_sales.csv")

# Sales by Region
region_sales = df.groupby('Region')['Total Sales'].sum()
region_sales.to_csv("eda_output/region_sales.csv")

# Monthly Sales
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Total Sales'].sum()
monthly_sales.to_csv("eda_output/monthly_sales.csv")

# -------------------------------
# 3. VISUALIZATIONS (SAVE IMAGES)
# -------------------------------

# Category Sales Bar Chart
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("eda_output/category_sales.png")
plt.close()

# Region Sales Pie Chart
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("eda_output/region_sales.png")
plt.close()

# Monthly Sales Line Chart
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("eda_output/monthly_sales.png")
plt.close()

# -------------------------------
# 4. CORRELATION
# -------------------------------

corr = df.corr(numeric_only=True)
corr.to_csv("eda_output/correlation_matrix.csv")

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("eda_output/correlation_heatmap.png")
plt.close()

# -------------------------------
# 5. SCATTER PLOT
# -------------------------------

plt.figure()
plt.scatter(df['Quantity'], df['Total Sales'])
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.title("Quantity vs Sales")
plt.tight_layout()
plt.savefig("eda_output/quantity_vs_sales.png")
plt.close()

print("EDA Completed! All outputs saved in 'eda_output' folder.")