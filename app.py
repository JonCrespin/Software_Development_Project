import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df= pd.read_csv('vgchartz_2024.csv')

st.header("Video Game Sales Dashboard")
st.write("Explore video game sales by platform, genre, and region!")

df= df.drop(df.columns[0], axis =1)
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce')
df['last_update'] = pd.to_datetime(df['last_update'], format='%Y-%m-%d', errors='coerce')


start_year, end_year = 2000, 2024
console_choice = df[
    (df['release_date'].dt.year >= start_year) & 
    (df['release_date'].dt.year <= end_year)
]['console'].unique()
console_choice.sort()
selected_menu = st.selectbox('Select an console',console_choice)

df_filtered = df[(df.console == selected_menu) ]
                 
st.dataframe(df_filtered)

st.header('Distribution of Price per Genre per Region')
st.write("""
###### Let's analyze what influences price the most. We will check how distribution of price varies depending on genre per region.
""")

sales_columns = ['na_sales', 'jp_sales', 'pal_sales', 'other_sales']

selected_region = st.selectbox('Split for price distribution',sales_columns)


fig1 = px.scatter(df_filtered, x='genre', y=selected_region, color='genre', title=f'{selected_region} Distribution by Genre')
fig1.update_layout(title= "<b> Split of price by {}</b>".format(selected_region))

st.plotly_chart(fig1)