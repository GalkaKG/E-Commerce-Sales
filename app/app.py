import streamlit as st

from etl.extract import load_from_postgres

st.title("E-commerce Data Dashboard")
st.write("...")

df = load_from_postgres()

st.dataframe(df)


# Filter by date range
start_date = st.date_input("Start Date", df["Date"].min())
end_date = st.date_input("End Date", df["Date"].max())

# Filter the dataframe based on the date range
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
st.dataframe(filtered_df)


categories = df['Category'].unique()
selected_category = st.selectbox("Select Category", categories)

filtered_df = df[df["Category"] == selected_category]
st.dataframe(filtered_df)

import plotly.express as px

# Sales over time
fig = px.line(filtered_df, x="Date", y="Amount", title="Sales Over Time")
st.plotly_chart(fig)


import seaborn as sns
import matplotlib.pyplot as plt

# Category distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=filtered_df, x='Category')
st.pyplot()


