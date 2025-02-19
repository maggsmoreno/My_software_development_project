import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("notebooks/vehicles_us.csv")  

st.write("### Preview of Dataset")
st.dataframe(df.head())  

