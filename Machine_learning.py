import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from utils import load_data, clean_data

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------
# LOAD DATA
# ---------------------------------------
df = load_data()
df = clean_data(df)

st.title("🤖 Demand Prediction using Machine Learning")

st.markdown("---")

# ---------------------------------------
# PREPARE DATA
# ---------------------------------------

ml_df = df.copy()

encoder = LabelEncoder()

categorical_columns = [
    "Category",
    "Sub-Category",
    "Region",
    "Segment"
]

for col in categorical_columns:
    ml_df[col] = encoder.fit_transform(ml_df[col])

X = ml_df[
    [
        "Sales",
        "Discount",
        "Profit",
        "Category",
        "Sub-Category",
        "Region",
        "Segment"
    ]
]

y = ml_df["Quantity"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------
# LINEAR REGRESSION
# ---------------------------------------

linear = LinearRegression()

linear.fit(X_train, y_train)

linear_pred = linear.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_pred)
linear_rmse = mean_squared_error(y_test, linear_pred) ** 0.5
linear_r2 = r2_score(y_test, linear_pred)

# ---------------------------------------
# RANDOM FOREST
# ---------------------------------------

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = mean_squared_error(y_test, rf_pred) ** 0.5
rf_r2 = r2_score(y_test, rf_pred)

# ---------------------------------------
# RESULTS
# ---------------------------------------

st.header("📊 Model Performance")

results = pd.DataFrame(
    {
        "Model": [
            "Linear Regression",
            "Random Forest"
        ],
        "MAE": [
            linear_mae,
            rf_mae
        ],
        "RMSE": [
            linear_rmse,
            rf_rmse
        ],
        "R² Score": [
            linear_r2,
            rf_r2
        ]
    }
)

st.dataframe(results, use_container_width=True)

st.markdown("---")

# ---------------------------------------
# BEST MODEL
# ---------------------------------------

best_model = "Random Forest" if rf_r2 > linear_r2 else "Linear Regression"

st.success(f"🏆 Best Performing Model: {best_model}")

st.markdown("---")

# ---------------------------------------
# USER PREDICTION
# ---------------------------------------

st.header("🔮 Predict Product Demand")

sales = st.number_input("Sales", value=1000.0)

discount = st.slider("Discount", 0.0, 1.0, 0.1)

profit = st.number_input("Profit", value=200.0)

category = st.selectbox(
    "Category",
    df["Category"].unique()
)

subcategory = st.selectbox(
    "Sub-Category",
    df["Sub-Category"].unique()
)

region = st.selectbox(
    "Region",
    df["Region"].unique()
)

segment = st.selectbox(
    "Segment",
    df["Segment"].unique()
)

if st.button("Predict Demand"):

    category = encoder.fit(df["Category"]).transform([category])[0]
    subcategory = encoder.fit(df["Sub-Category"]).transform([subcategory])[0]
    region = encoder.fit(df["Region"]).transform([region])[0]
    segment = encoder.fit(df["Segment"]).transform([segment])[0]

    sample = pd.DataFrame(
        [[
            sales,
            discount,
            profit,
            category,
            subcategory,
            region,
            segment
        ]],
        columns=X.columns
    )

    prediction = rf.predict(sample)

    st.success(f"📦 Predicted Quantity (Demand): {prediction[0]:.2f}")