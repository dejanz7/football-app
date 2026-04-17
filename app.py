import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("📊 Data Dashboard")

st.write("Basic interactive analytics app")

# ========================
# SIDEBAR
# ========================
st.sidebar.header("Controls")

num_points = st.sidebar.slider("Number of data points", 10, 100, 50)

# ========================
# GENERATE DATA
# ========================
data = pd.DataFrame({
    "x": np.arange(num_points),
    "y": np.random.randn(num_points).cumsum()
})

# ========================
# MAIN CONTENT
# ========================
st.subheader("Line Chart")
st.line_chart(data.set_index("x"))

st.subheader("Data Table")
st.dataframe(data)

# ========================
# USER INPUT
# ========================
st.subheader("Add your value")

value = st.number_input("Enter a number", 0, 100, 10)

if st.button("Show value"):
    st.success(f"You entered: {value}")
