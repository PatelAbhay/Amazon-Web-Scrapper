import requests
from requests.api import request
from bs4 import BeautifulSoup

URL = ""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

tracking_page = requests.get(URL, headers=headers)

soup = BeautifulSoup(tracking_page.content, 'html.parser')
