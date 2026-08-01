import streamlit as st
import matplotlib.pyplot as plt

from utils import (
    load_data,
    clean_data,
    total_sales,
    total_profit,
    total_orders,
    total_quantity
)

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="Sales Analysis",
    page_icon="📈",
    layout="wide"
)

# ---------------------------------------
# LOAD DATA
# ---------------------------------------
df = load_data()
df = clean_data(df)

# ---------------------------------------
# TITLE
# ---------------------------------------
st.title("📈 Sales Analysis Dashboard")

st.markdown("Analyze overall sales performance using KPIs and visualizations.")

st.markdown("---")

# ---------------------------------------
# KPI CARDS
# ---------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"${total_sales(df):,.2f}"
    )

with col2:
    st.metric(
        "📈 Total Profit",
        f"${total_profit(df):,.2f}"
    )

with col3:
    st.metric(
        "🛒 Orders",
        total_orders(df)
    )

with col4:
    st.metric(
        "📦 Quantity Sold",
        total_quantity(df)
    )

st.markdown("---")

# ---------------------------------------
# MONTHLY SALES TREND
# ---------------------------------------
st.subheader("📅 Monthly Sales Trend")

monthly_sales = (
    df.groupby("Month Number")["Sales"]
      .sum()
      .reset_index()
      .sort_values("Month Number")
)

month_names = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

monthly_sales["Month"] = month_names

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o",
    linewidth=3
)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales Trend")

st.pyplot(fig)

st.markdown("---")

# ---------------------------------------
# YEARLY SALES
# ---------------------------------------
st.subheader("📆 Year-wise Sales")

year_sales = (
    df.groupby("Year")["Sales"]
      .sum()
)

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    year_sales.index.astype(str),
    year_sales.values
)

ax.set_title("Year-wise Sales")

st.pyplot(fig)

st.markdown("---")

# ---------------------------------------
# SALES BY CATEGORY
# ---------------------------------------
st.subheader("🛍 Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    category_sales.index,
    category_sales.values
)

ax.set_title("Category-wise Sales")

st.pyplot(fig)

st.markdown("---")

# ---------------------------------------
# SALES BY SEGMENT
# ---------------------------------------
st.subheader("👥 Sales by Customer Segment")

segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
)

fig, ax = plt.subplots(figsize=(8,5))

ax.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct="%1.1f%%"
)

ax.set_title("Sales Distribution by Segment")

st.pyplot(fig)

st.markdown("---")

# ---------------------------------------
# SALES TABLE
# ---------------------------------------
st.subheader("📋 Sales Summary")

summary = df.groupby("Category")[["Sales","Profit","Quantity"]].sum()

st.dataframe(
    summary,
    use_container_width=True
)

st.success("✅ Sales Analysis Completed Successfully")