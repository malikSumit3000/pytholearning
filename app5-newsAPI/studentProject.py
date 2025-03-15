import streamlit as st
import requests
import os

api_key = os.getenv("NASA_API_KEY")

url = ('https://api.nasa.gov/planetary/apod?'
       'api_key='
       f'{api_key}')

request = requests.get(url)

response = request.json()

get_image = requests.get(response["hdurl"])

with open("image.jpg", "wb") as file:
    file.write(get_image.content)

description = response["explanation"]

st.title(response['title'])
st.image("image.jpg", width=500)
st.write(description)
