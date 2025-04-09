import os
import smtplib
import imghdr
from email.message import EmailMessage

user_name = "smalikfab25@gmail.com"
receiver = "smalikfab25@gmail.com"
password = os.getenv("PASSWORD")


def sending_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "Motion Detected!"
    email_message.set_content("Hey, we just detected a motion!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(user_name, password)
    gmail.sendmail(user_name, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    sending_email(image_path="images/6.png")
