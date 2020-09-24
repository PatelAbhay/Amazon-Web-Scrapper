import requests
import os
from bs4 import BeautifulSoup
import time

path = os.getcwd()
dir_list = os.listdir(path)
saved_links = []

if "savedProductLinks.txt" in dir_list:
    saved_file = open("savedProductLinks.txt", "r")
    line = saved_file.readline()

    while line:
        p_name = line.split(" : ")[0]
        p_link = line.split(" : ")[1]
        saved_links.append([p_name, p_link])
        line = saved_file.readline()

    saved_file.close()
    print("Loaded saved links from file\n")


def track():
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    for i in range(0, len(saved_links)):
        track_page = requests.get(saved_links[i][1], headers=header)
        scrapper = BeautifulSoup(track_page.content, 'html.parser')

        product_title = scrapper.find(id="productTitle").getText().strip()
        product_price = scrapper.find(
            id="priceblock_ourprice").getText().strip()
        available = scrapper.find(id="availability").getText().strip()

        print("\nProduct Name : " + product_title)
        print("Current Listing Price : " + product_price)
        print("Availability : " + available + "\n")


def saveList():
    my_file = open("savedProductLinks.txt", "a")
    for link in saved_links:
        my_file.write(link[0] + " : " + link[1])
    my_file.close()


while True:
    print("Options List")
    print("1 : Add Item to Track")
    print("2 : Save Product List to Text File")
    print("3 : Remove Item from Product List")
    print("4 : Track in the background")
    print("5 : Print Product List")
    print("6 : Clear Product List")
    print("7 : Quit Program")

    choice = input("What would you like to do?\n")

    if choice == "1":
        product_name = input("Enter the product name:\n")
        URL = input("Enter the link of the product:\n")
        saved_links.append([product_name, URL])
        print("This product will be tracked\n")
    elif choice == "2":
        saveList()
    elif choice == "3":
        remove_name = input("Enter the name of the product:\n")
        prev_len = len(saved_links)
        for i in range(0, len(saved_links)):
            if remove_name == saved_links[i][0]:
                saved_links.pop(i)
                break
        if prev_len == len(saved_links):
            print("The Product Name was not found!")

    elif choice == "4":
        try:
            while True:
                track()
                time.sleep(5)
        except KeyboardInterrupt:
            pass
    elif choice == "5":
        if len(saved_links) == 0:
            print("Product List is Empty")
        else:
            for link in saved_links:
                print(link)
        print()
    elif choice == "6":
        saved_links.clear()
        print("Product List has been cleared")
        if "savedProductLinks.txt" in dir_list:
            saved_file = open("savedProductLinks.txt", "w").close()
            print("Cleared Contents in File")
        print()
    elif choice == "7":
        quit()
    else:
        print("That is not a valid option\n")
