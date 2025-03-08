import streamlit as st
import requests

Api_key = 'lu8mCFZwsiWCpqYLA7pPZw7G0ZNJXAIM245998dC'

url = ('https://api.nasa.gov/planetary/apod?'
       'api_key='
       f'{Api_key}')

request = requests.get(url)

response = request.json()

get_image = requests.get(response["hdurl"])

with open("image.jpg", "wb") as file:
    file.write(get_image.content)

description = response["explanation"]

st.title(response['title'])
st.image("image.jpg", width=500)
st.write(description)
