import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df= pd.read_csv('vgchartz_2024.csv')

st.header("Video Game Sales Dashboard")
st.write("Explore video game sales by platform, genre, and region!")