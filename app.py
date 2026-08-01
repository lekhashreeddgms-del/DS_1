import streamlit as st

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="E-Commerce Sales Analysis & Demand Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("📊 Navigation")
st.sidebar.success("Select a page from the sidebar.")

st.sidebar.markdown("---")
st.sidebar.write("**Project:**")
st.sidebar.write("E-Commerce Sales Analysis & Demand Prediction")

st.sidebar.markdown("---")
st.sidebar.info(
    """
This dashboard analyzes historical sales data and predicts future product demand using Machine Learning.
"""
)

# -------------------------------
# MAIN TITLE
# -------------------------------
st.title("📊 E-Commerce Sales Analysis & Demand Prediction")

st.markdown("""
Welcome to the interactive dashboard for analyzing e-commerce sales data.

This project uses **Exploratory Data Analysis (EDA)** and **Machine Learning**
to discover valuable business insights and forecast future product demand.
""")

st.markdown("---")

# -------------------------------
# PROJECT OVERVIEW
# -------------------------------
st.header("📌 Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Objective")

    st.write("""
- Analyze historical sales data
- Identify top-selling products
- Study region-wise performance
- Discover seasonal demand patterns
- Predict future product demand
- Optimize inventory management
""")

with col2:
    st.subheader("🛠 Technologies Used")

    st.write("""
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
""")

st.markdown("---")

# -------------------------------
# WORKFLOW
# -------------------------------
st.header("📈 Project Workflow")

st.markdown("""
1️⃣ Data Collection

⬇

2️⃣ Data Cleaning

⬇

3️⃣ Exploratory Data Analysis (EDA)

⬇

4️⃣ Machine Learning

⬇

5️⃣ Demand Prediction

⬇

6️⃣ Business Insights
""")

st.markdown("---")

# -------------------------------
# FEATURES
# -------------------------------
st.header("🚀 Dashboard Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📂 Dataset
- View Dataset
- Missing Values
- Data Types
""")

with col2:
    st.success("""
### 📊 Sales Analysis
- Monthly Sales
- Top Products
- Region-wise Sales
""")

with col3:
    st.warning("""
### 🤖 Machine Learning
- Linear Regression
- Random Forest
- Demand Prediction
""")

st.markdown("---")

# -------------------------------
# BUSINESS BENEFITS
# -------------------------------
st.header("💼 Business Benefits")

st.write("""
✔ Better Inventory Planning

✔ Reduce Stock-Outs

✔ Improve Sales Forecasting

✔ Increase Profitability

✔ Data-Driven Decision Making
""")

st.markdown("---")

st.success("✅ Project setup completed successfully!")

st.caption("Developed using Streamlit | E-Commerce Sales Analysis Dashboard")
