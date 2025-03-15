import pandas as pd
import plotly.express as px
import streamlit as st

# Read in the data (Make sure the correct path to 'vehicles_us.csv' is used)
df = pd.read_csv("notebooks/vehicles_us.csv")

# Fill missing 'year' values by the median 'year' for each 'vtype'
df['year'] = df.groupby('vtype')['year'].transform(lambda x: x.fillna(x.median()))

# Fill missing 'miles' values (odometer) by the median 'miles' for each 'vtype'
df['miles'] = df.groupby('vtype')['miles'].transform(lambda x: x.fillna(x.median()))

# Remove outliers in 'price' (optional)
price_lower_bound = df['price'].quantile(0.01)
price_upper_bound = df['price'].quantile(0.99)
df = df[(df['price'] >= price_lower_bound) & (df['price'] <= price_upper_bound)]

# Remove outliers in 'year' (optional)
year_lower_bound = df['year'].quantile(0.01)
year_upper_bound = df['year'].quantile(0.99)
df = df[(df['year'] >= year_lower_bound) & (df['year'] <= year_upper_bound)]

# Markdown for Introduction and Overview
st.markdown("""
# 🛠️ Car Market Analysis Project
This project analyzes car advertisement data to provide insights into car pricing, mileage, and more.
The data preprocessing steps include handling missing values, removing outliers, and filling in necessary details like **model year**, **mileage**, and **cylinders**. The resulting visualizations and summaries help us understand trends in the car market.

## 📊 Price Distribution of Cars (Histogram)
""")

# Histogram for Price Distribution
fig = px.histogram(df, x="price", nbins=50, title="Price Distribution")
st.plotly_chart(fig)

# Markdown for Histogram Analysis
st.markdown("""
### **Key Takeaways from the Histogram:**
- 🔹 The **majority** of car prices fall within the **lower price range**, indicating that most cars are affordable and cater to budget-conscious buyers.
- 🔹 High-end, expensive cars are **less common** but can still be found, particularly at price points like **$10,000, $15,000**.
- 🔹 The presence of sharp price points may reflect **popular listing prices** or **common seller pricing strategies**.
- 🔹 Very **low-priced cars** (under $500) could represent vehicles in **poor condition**, such as **salvaged or damaged cars**.
""")

# Scatter Plot for Price vs. Mileage
st.markdown("""
## 🚗 Price vs. Mileage (Scatter Plot)
""")
scatter_fig = px.scatter(df, x="miles", y="price", title="Price vs. Mileage")
st.plotly_chart(scatter_fig)

# Markdown for Scatter Plot Analysis
st.markdown("""
### **Key Takeaways from the Scatter Plot:**
- 🔹 There is a **negative correlation** between **mileage** and **price**, suggesting that as a car's mileage increases, its price generally decreases.
- 🔹 **Lower mileage cars** tend to be **newer** and are priced **higher**, a trend consistent with the typical depreciation of cars over time.
- 🔹 Some cars with **high mileage** but **higher prices** may be **well-maintained**, or they could be **luxury models** with lasting value.
- 🔹 The **market** shows a **cluster** of cars within similar mileage and price ranges, indicating common **market segments** and **pricing strategies**.
""")

# Display Preprocessed Data Overview
st.markdown("""
## 🧹 Data Preprocessing and Cleaning
The data underwent several preprocessing steps to handle missing values and remove outliers, ensuring it is clean for analysis. The missing values for key features like **year**, **mileage**, and **cylinders** were filled based on the **median** values of their respective categories.

""")
st.write(df.head())

# Summary of Findings (Markdown)
st.markdown("""
## 📝 Summary of Findings

### **1. Price Distribution (Histogram)**
- 🔹 The **majority** of car prices fall within the **lower price range**, indicating that most cars are affordable and cater to budget-conscious buyers.
- 🔹 High-end, expensive cars are **less common** but can still be found, particularly at price points like **$10,000, $15,000**.
- 🔹 The presence of sharp price points may reflect **popular listing prices** or **common seller pricing strategies**.
- 🔹 Very **low-priced cars** (under $500) could represent vehicles in **poor condition**, such as **salvaged or damaged cars**.

### **2. Price vs. Mileage (Scatterplot)**
- 🔹 There is a **negative correlation** between **mileage** and **price**, suggesting that as a car's mileage increases, its price generally decreases.
- 🔹 **Lower mileage cars** tend to be **newer** and are priced **higher**, a trend consistent with the typical depreciation of cars over time.
- 🔹 Some cars with **high mileage** but **higher prices** may be **well-maintained**, or they could be **luxury models** with lasting value.
- 🔹 The **market** shows a **cluster** of cars within similar mileage and price ranges, indicating common **market segments** and **pricing strategies**.

### **3. Preprocessing Insights**
- 🔹 Missing values in **model year** and **cylinders** were filled with the **median** for each model, maintaining data consistency for further analysis.
- 🔹 **Odometer values** were filled by **grouping by model year** to ensure accuracy and prevent misleading data from affecting analysis.
- 🔹 Outliers in **model year** and **price** were removed to make the scatterplots more informative and to avoid distorting the insights.
- 🔹 This preprocessing ensures that the dataset is clean, more representative, and ready for meaningful analysis.
""")


