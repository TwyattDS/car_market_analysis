import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Streamlit App
st.title("Car Market Analysis Dashboard 🚗")
st.markdown("Explore the trends in car sales data.")

# Introduction Section
st.markdown("""
This dashboard provides insights into the used car market based on real-world data.
You can explore different aspects such as pricing trends, mileage distribution, and more.
""")

# Histogram (Price Distribution)
st.subheader("Price Distribution")
fig = px.histogram(df, x="price", title="Distribution of Car Prices")
st.plotly_chart(fig)

st.markdown("""
### 📝 Interpretation of the Histogram
- The majority of cars are priced below a certain threshold.
- There might be some **outliers** (very expensive cars) affecting the distribution.
- This helps us understand the overall price range in the dataset.
""")

# Scatter plot (Price vs. Mileage)
st.subheader("Price vs. Mileage")
fig2 = px.scatter(df, x="miles", y="price", title="Price vs. Mileage")
st.plotly_chart(fig2)

st.markdown("""
### 📝 Interpretation of the Scatter Plot
- Typically, cars with **higher mileage** are sold for **lower prices**.
- There are some exceptions where certain cars retain value despite higher mileage.
- Understanding this relationship helps buyers and sellers set realistic expectations.
""")


# Checkbox to preview dataset
if st.checkbox("Show Dataset Preview"):
    st.write(df.head())
