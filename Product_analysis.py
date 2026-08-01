import streamlit as st
import matplotlib.pyplot as plt

from utils import load_data, clean_data

# ------------------------------------
# PAGE CONFIG
# ------------------------------------
st.set_page_config(
    page_title="Product Analysis",
    page_icon="📦",
    layout="wide"
)

# ------------------------------------
# LOAD DATA
# ------------------------------------
df = load_data()
df = clean_data(df)

# ------------------------------------
# TITLE
# ------------------------------------
st.title("📦 Product Analysis Dashboard")

st.markdown("Analyze product performance based on Sales, Quantity and Profit.")

st.markdown("---")

# ------------------------------------
# TOP 10 PRODUCTS BY SALES
# ------------------------------------
st.subheader("🏆 Top 10 Products by Sales")

top_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(top_sales.index, top_sales.values)
ax.invert_yaxis()
ax.set_xlabel("Sales")
ax.set_title("Top 10 Products by Sales")

st.pyplot(fig)

st.markdown("---")

# ------------------------------------
# TOP 10 PRODUCTS BY QUANTITY
# ------------------------------------
st.subheader("📦 Top 10 Products by Quantity Sold")

top_quantity = (
    df.groupby("Product Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(top_quantity.index, top_quantity.values)
ax.invert_yaxis()
ax.set_xlabel("Quantity")

st.pyplot(fig)

st.markdown("---")

# ------------------------------------
# TOP 10 PRODUCTS BY PROFIT
# ------------------------------------
st.subheader("💰 Top 10 Most Profitable Products")

top_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(top_profit.index, top_profit.values)
ax.invert_yaxis()
ax.set_xlabel("Profit")

st.pyplot(fig)

st.markdown("---")

# ------------------------------------
# SALES BY SUB-CATEGORY
# ------------------------------------
# ------------------------------------
# SALES BY SUB-CATEGORY
# ------------------------------------
st.subheader("📂 Sales by Sub-Category")

subcategory = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=True)
)

fig, ax = plt.subplots(figsize=(12,8))

ax.barh(
    subcategory.index,
    subcategory.values
)

ax.set_xlabel("Sales")
ax.set_ylabel("Sub-Category")
ax.set_title("Sales by Sub-Category")

st.pyplot(fig)