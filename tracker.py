import requests
from requests.api import request
from bs4 import BeautifulSoup
import smtplib
import time


def send_email(user_email, user_password, product_name, product_price, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user_email, user_password)

    email_subject = product_name + " has dropped to " + product_price
    email_body = "Click the link to see the posting " + URL

    email = f"Subject: {email_subject}\n\n{email_body}"

    server.sendmail(
        user_email,
        user_email,
        email
    )

    server.quit()


def track(URL, user_email, user_password, max_price):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }

    tracking_page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(tracking_page.content, 'html.parser')

    product_name = soup.find(id="productTitle").get_text()
    product_price = soup.find(id="priceblock_ourprice").get_text()

    if product_price is not None and product_name is not None:
        print(product_name.strip())
        print(product_price.strip())

        num_price = float(product_price[5:])

        if num_price < float(max_price):
            send_email(user_email, user_password,
                       product_name.strip(), product_price.strip(), URL)
            return 1
        return 0
    return -1


URL = input("Enter the URL if the Amazon Post you wish to track\n")
user_email = input("Enter your email\n")
user_password = input("Enter your email password\n")
max_price = float(input("Enter the price at which we should send an email\n"))

while True:
    result = track(URL, user_email, user_password, max_price)
    if result == 1:
        print("PRICE DROPPED! WE SENT YOU AN EMAIL!")
        break
    if result == -1:
        print("There was an error reading the post")
        break
    time.sleep(60*5)  # checks post every 5 minutes
