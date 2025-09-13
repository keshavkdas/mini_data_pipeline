# app.py
import pandas as pd
from sqlalchemy import create_engine
from constants import mysql_uri
import streamlit as st
import plotly.express as px

# Connect to MySQL
engine = create_engine(mysql_uri)
df = pd.read_sql("SELECT * FROM sales", engine)

# Transform if needed
df['revenue'] = df['sales'] * df['quantity']

# Streamlit dashboard
st.title("Sales Dashboard")
st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Revenue by Product")
fig = px.bar(df, x='product', y='revenue', color='region')
st.plotly_chart(fig)

# Filter example
product = st.selectbox("Select Product", df['product'].unique())
st.subheader(f"Details for {product}")
st.dataframe(df[df['product'] == product])

