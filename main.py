import streamlit as st
import plotly.express as px
from backend import getdata
st.title("Welcome to weather forecasting!")


place = st.text_input('Place' ' - ')

forecast_days = st.slider(label='Forecast days', min_value=1, max_value=5, help="Select the number of forecasted days")

category = st.selectbox('Category', ("Temperature", "Sky"))


if place:

    try:

        data = getdata(place, forecast_days)
        st.subheader(f"{category} for the next {forecast_days} days in {place}")

        if category == 'Temperature':
            processed_data = [{"datetime": entry["dt_txt"], "temperature": entry["main"]["temp"]/10} for entry in data]
            x_axis = [entry["datetime"] for entry in processed_data]
            y_axis = [entry["temperature"] for entry in processed_data]
            figure = px.line(x=x_axis, y=y_axis, labels={'x': 'dates', 'y': 'temperature(C)'})
            st.plotly_chart(figure)

        if category == 'Sky':
            processed_data = [entry['weather'][0]['main'] for entry in data]
            images = {'Clear': 'images/clear.png', 'Snow': 'images/snow.png', 'Rain': 'images/rain.png',
                      'Clouds': 'images/cloud.png'}
            image_path = [images[condition] for condition in processed_data]
            st.image(image_path, width=120)

    except KeyError:
        st.write("That place is not in our repository or  does not exist.")



