import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('vehicles_us.csv')

st.write("### Preview of Dataset")

#st.dataframe(df.head())  

#df.dropna(subset=["model_year", "cylinders", "odometer"], inplace=True)
st.plotly_chart(px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices",labels={"price": "Price ($)"}, color_discrete_sequence=["blue"]))
st.plotly_chart(px.histogram(df, x="model_year", nbins=30, title="Distribution of Vehicle Model Years", labels={"model_year": "Model Year"}, color_discrete_sequence=["green"]))
st.plotly_chart(px.scatter(df, x="odometer", y="price", title="Odometer vs. Price", labels={"odometer": "Odometer (miles)", "price": "Price ($)"},color="model_year", opacity=0.7))
st.plotly_chart(px.scatter(df, x="model_year", y="price", title="Model Year vs. Price",labels={"model_year": "Model Year", "price": "Price ($)"},color="fuel", opacity=0.7))

car_type_counts = df["type"].value_counts().reset_index()
car_type_counts.columns = ["Car Type", "Count"]  

st.plotly_chart(px.bar(car_type_counts, x="Car Type", y="Count",title="Most Common Car Types", labels={"Car Type": "Car Type", "Count": "Count"},color="Car Type", color_discrete_sequence=px.colors.qualitative.Set3))


st.header("Exploratory Data Analysis of Vehicles Dataset")

st.subheader("Dataset Overview")

st.write("This dataset contains information on used vehicles listed for sale in the US.")

st.plotly_chart(px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices"))

 #st.plotly_chart(px.histogram(df, x='price', nbins=50, title="Car Prices"))

st.title("Exploratory Data Analysis")

show_data = st.checkbox("Show DataFrame")

if show_data:
    st.write("Here is my dataset:")
    st.dataframe(df)
else:
    st.write("Check the box above to display the data.")

g = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
st.plotly_chart(g)