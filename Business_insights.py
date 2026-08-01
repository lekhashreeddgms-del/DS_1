import streamlit as st
from utils import load_data, clean_data

st.set_page_config(
    page_title="Business Insights",
    page_icon="💼",
    layout="wide"
)

df = clean_data(load_data())

st.title("💼 Business Insights")

st.markdown("### Executive Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", f"${df['Sales'].sum():,.2f}")

with col2:
    st.metric("Total Profit", f"${df['Profit'].sum():,.2f}")

with col3:
    st.metric("Total Orders", df["Order ID"].nunique())

with col4:
    st.metric("Products Sold", int(df["Quantity"].sum()))

st.divider()

st.subheader("🏆 Top 5 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

st.dataframe(top_products, use_container_width=True)

st.divider()

st.subheader("🌍 Top 5 States")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

st.dataframe(top_states, use_container_width=True)

st.divider()

st.subheader("📌 Key Findings")

st.success("""
• Technology products generated the highest revenue.

• A small number of products contribute significantly to total sales.

• Sales differ across regions.

• Discounts improve sales but can reduce profit.

• Random Forest performed better than Linear Regression for demand prediction.
""")

st.divider()

st.subheader("💡 Recommendations")

st.info("""
✅ Maintain higher inventory for high-demand products.

✅ Reduce excessive discounts.

✅ Increase marketing in low-performing regions.

✅ Forecast demand before seasonal peaks.

✅ Use Machine Learning predictions for inventory planning.
""")

st.divider()

st.subheader("🎯 Conclusion")

st.write("""
This project analyzed historical e-commerce sales data and developed a demand prediction model using Machine Learning.

The dashboard helps businesses understand customer behavior, identify high-performing products and regions, optimize inventory, and make data-driven decisions.

The Random Forest model achieved the best prediction performance and is recommended for future demand forecasting.
""")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Cleaned Dataset",
    data=csv,
    file_name="Cleaned_Superstore.csv",
    mime="text/csv"
)

st.success("Dashboard Completed Successfully! 🎉")