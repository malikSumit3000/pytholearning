import requests
from send_email import sending_email
import os

api_key = os.getenv("API_KEY")

topic = "Business"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2025-02-04&sortBy=publishedAt&"
       "apiKey=23f98aadee7d4636a4b8a73f8627daeb&"
       "language=en")

request = requests.get(url)

content = request.json()

message = "Subject: Today's news" + "\n" + ""
for article in content["articles"][:20]:
    message = message + article["title"] + "\n" + str(article["description"]) \
              + "\n" + article["url"] \
              + 2 * "\n"

message = message.encode("utf-8")
sending_email(message=message)
