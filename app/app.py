# import streamlit as st

# from etl.extract import load_from_postgres
# from utils import query

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns


# st.title("E-commerce Data Dashboard")

# df = load_from_postgres(query)


# # Filter by date range
# st.write("Filter by date range")
# start_date = st.date_input("Start Date", df["date"].min())
# end_date = st.date_input("End Date", df["date"].max())

# start_date = pd.to_datetime(start_date)
# end_date = pd.to_datetime(end_date)

# # Filter the dataframe based on the date range
# filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
# st.dataframe(filtered_df)

# st.write("Categories")
# categories = df['category'].unique()
# selected_category = st.selectbox("Select Category", categories)

# filtered_df = df[df["category"] == selected_category]
# st.dataframe(filtered_df)

# # Create a seaborn count plot and display it 
# plt.figure(figsize=(6, 6))
# sns.countplot(x=df['size'], data=df, palette='Set1')

# plt.xlabel('Size')
# plt.ylabel('Number of orders')
# plt.title('Top selling sizes of products')
# plt.xticks(rotation=50)

# st.pyplot(plt)

# # Sales by Category
# plt.figure(figsize=(8, 6))
# sns.barplot(x="category", y="amount", data=filtered_df, palette="Set2")
# plt.title('Sales by Category')
# st.pyplot(plt)



import streamlit as st

from etl.extract import load_from_postgres
from utils import query

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("E-commerce Data Dashboard")

df = load_from_postgres(query)

# Filter by date range
st.write("Filter by date range")
start_date = st.date_input("Start Date", df["date"].min())
end_date = st.date_input("End Date", df["date"].max())

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter the dataframe based on the date range
filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
st.dataframe(filtered_df)

st.write("Categories")
categories = df['category'].unique()
selected_category = st.selectbox("Select Category", categories)

filtered_df = df[df["category"] == selected_category]
st.dataframe(filtered_df)

# Create the category distribution plot (Bar plot)
fig1, ax1 = plt.subplots(figsize=(6, 6))
sns.countplot(x='size', data=filtered_df, palette='Set1', ax=ax1)
ax1.set_xlabel('Size')
ax1.set_ylabel('Number of Orders')
ax1.set_title('Top Selling Sizes of Products')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=50)

# Create the sales over time plot (Line plot)
fig2, ax2 = plt.subplots(figsize=(8, 6))
sales_by_date = filtered_df.groupby('date').size()
sales_by_date.plot(kind='line', ax=ax2)
ax2.set_xlabel('Date')
ax2.set_ylabel('Number of Orders')
ax2.set_title('Sales Over Time')

# Display the two plots side by side using columns
col1, col2 = st.columns(2)

with col1:
    st.write("Category Distribution")
    st.pyplot(fig1)

with col2:
    st.write("Sales Over Time")
    st.pyplot(fig2)
