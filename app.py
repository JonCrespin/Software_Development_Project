import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df= pd.read_csv('vgchartz_2024.csv')

st.header("Video Game Sales Dashboard")
st.write("Explore video game sales by platform, genre, and region!")

df= df.drop(df.columns[0], axis =1)
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce')
df = df.dropna(subset=['release_date'])
df['last_update'] = pd.to_datetime(df['last_update'], format='%Y-%m-%d', errors='coerce')
df = df.dropna(subset=['last_update'])

median_critic_score = df['critic_score'].median()
df['critic_score'] = df['critic_score'].fillna(median_critic_score)
print(df['critic_score'].median())

df.loc[(df['title'] == 'My Friend Pedro') & (df['console']
.isin(['NS', 'PC'])), 'developer'] = 'DeadToast Entertainment'

df = df.dropna()

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
###### Let's analyze what influences price the most. 
We will check how distribution of price varies depending on genre and developer per region.
""")

sales_columns = ['na_sales', 'jp_sales', 'pal_sales', 'other_sales']

selected_region = st.selectbox('Split for price distribution',sales_columns)


fig1 = px.scatter(df_filtered, x='genre', y=selected_region, 
color='developer', title=f'{selected_region} Distribution by Genre')
fig1.update_layout(title= "<b> Split of price by {}</b>".format(selected_region))

st.plotly_chart(fig1)
  
def sales_vs_critic_score(df, include_genre=False):
    required_columns = ['critic_score', 'total_sales']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("DataFrame must include 'critic_score' and 'total_sales' columns.")
    
    analysis_df = df[['critic_score', 'total_sales']].copy()
    if include_genre:
        if 'genre' not in df.columns:
            raise ValueError("DataFrame must include 'genre' column to use include_genre=True.")
        analysis_df['genre'] = df['genre']
    
    analysis_df = analysis_df.dropna(subset=['critic_score', 'total_sales'])
    return analysis_df

# Sales vs. Critic Score visualization
include_genre = st.checkbox("Include Genre")

# Process data based on the checkbox
analysis_df = sales_vs_critic_score(df_filtered, include_genre=include_genre)

# Ensure that 'genre' is in the DataFrame before using it in the visualization
if include_genre and 'genre' in analysis_df.columns:
    fig2 = px.histogram(
        analysis_df,
        x='critic_score',
        y='total_sales',
        color='genre',
        nbins=20,
        title="Sales vs. Critic Score by Genre",
        labels={'critic_score': 'Critic Score', 'total_sales': 'Total Sales'}
    )
else:
    fig2 = px.histogram(
        analysis_df,
        x='critic_score',
        y='total_sales',
        nbins=20,
        title="Sales vs. Critic Score",
        labels={'critic_score': 'Critic Score', 'total_sales': 'Total Sales'}
    )

fig2.update_layout(bargap=0.1)
