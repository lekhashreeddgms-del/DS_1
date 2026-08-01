import pandas as pd
import streamlit as st

# ----------------------------------------
# LOAD DATA
# ----------------------------------------
@st.cache_data
def load_data():
    """
    Load the Superstore dataset from Excel.
    """

    df = pd.read_excel("Superstore.xlsx")

    return df


# ----------------------------------------
# CLEAN DATA
# ----------------------------------------
@st.cache_data
def clean_data(df):
    """
    Clean the dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Convert Order Date
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # Convert Ship Date
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Month
    df["Month"] = df["Order Date"].dt.month_name()

    # Month Number
    df["Month Number"] = df["Order Date"].dt.month

    # Year
    df["Year"] = df["Order Date"].dt.year

    # Quarter
    df["Quarter"] = df["Order Date"].dt.quarter

    return df


# ----------------------------------------
# KPI CALCULATIONS
# ----------------------------------------
def total_sales(df):
    return df["Sales"].sum()


def total_profit(df):
    return df["Profit"].sum()


def total_orders(df):
    return df["Order ID"].nunique()


def total_quantity(df):
    return df["Quantity"].sum()


# ----------------------------------------
# TOP PRODUCTS
# ----------------------------------------
def top_products(df):

    top = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return top


# ----------------------------------------
# REGION SALES
# ----------------------------------------
def region_sales(df):

    region = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return region


# ----------------------------------------
# CATEGORY SALES
# ----------------------------------------
def category_sales(df):

    category = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return category


# ----------------------------------------
# MONTHLY SALES
# ----------------------------------------
def monthly_sales(df):

    monthly = (
        df.groupby("Month Number")["Sales"]
        .sum()
        .reset_index()
    )

    month_names = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    monthly["Month"] = monthly["Month Number"].map(month_names)

    return monthly