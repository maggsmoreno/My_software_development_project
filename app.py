import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("notebooks/vehicles_us.csv")  

st.write("### Preview of Dataset")
st.dataframe(df.head())  

st.title("Exploratory Data Analysis")

show_data = st.checkbox("Show DataFrame")

if show_data:
    st.write("Here is my dataset:")
    st.dataframe(df)
else:
    st.write("Check the box above to display the data.")

g = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
st.plotly_chart(g)