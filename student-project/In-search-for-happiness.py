import streamlit as st
import plotly.express as px
import pandas as pd

st.title('In Search for Happiness')

x_axis = st.selectbox("Select the data for the X-axis", ('GDP', 'Happiness', 'Generosity'))
y_axis = st.selectbox("Select the data for the Y-axis", ('GDP', 'Happiness', 'Generosity'))

st.subheader(f"{x_axis} and {y_axis}")


def getdata(x_axis, y_axis):
    df = pd.read_csv("happy.csv")
    x_axis = x_axis.lower()
    y_axis = y_axis.lower()
    x_axis = df[f'{x_axis}']
    y_axis = df[f'{y_axis}']
    return x_axis, y_axis


X, Y = getdata(x_axis, y_axis)

figure = px.scatter(x=X, y=Y, labels={'x': f'{x_axis}', 'y': f'{y_axis}'})
st.plotly_chart(figure)
