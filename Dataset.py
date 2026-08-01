import streamlit as st
from utils import load_data, clean_data

# ------------------------------------
# PAGE CONFIGURATION
# ------------------------------------
st.set_page_config(
    page_title="Dataset Overview",
    page_icon="📂",
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
st.title("📂 Dataset Overview")

st.markdown("""
This page provides an overview of the **Superstore Dataset** used for
E-Commerce Sales Analysis and Demand Prediction.
""")

st.markdown("---")

# ------------------------------------
# DATASET SHAPE
# ------------------------------------
rows, cols = df.shape

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Rows", rows)

with col2:
    st.metric("Total Columns", cols)

st.markdown("---")

# ------------------------------------
# DATA PREVIEW
# ------------------------------------
st.subheader("👀 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

# ------------------------------------
# COLUMN NAMES
# ------------------------------------
st.subheader("📋 Column Names")

st.write(df.columns.tolist())

st.markdown("---")

# ------------------------------------
# DATA TYPES
# ------------------------------------
st.subheader("🔍 Data Types")

st.dataframe(df.dtypes.astype(str).reset_index().rename(
    columns={
        "index": "Column",
        0: "Data Type"
    }),
    use_container_width=True
)

st.markdown("---")

# ------------------------------------
# MISSING VALUES
# ------------------------------------
st.subheader("❓ Missing Values")

missing = df.isnull().sum().reset_index()

missing.columns = [
    "Column",
    "Missing Values"
]

st.dataframe(
    missing,
    use_container_width=True
)

st.markdown("---")

# ------------------------------------
# DUPLICATES
# ------------------------------------
st.subheader("🔁 Duplicate Rows")

duplicates = df.duplicated().sum()

st.metric(
    "Duplicate Rows",
    duplicates
)

st.markdown("---")

# ------------------------------------
# SUMMARY STATISTICS
# ------------------------------------
st.subheader("📊 Summary Statistics")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.markdown("---")

st.success("✅ Dataset loaded and cleaned successfully!")