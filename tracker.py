import requests
import os

path = os.getcwd()
dir_list = os.listdir(path)
saved_links = []

while True:
    if "savedProductLinks.txt" in dir_list:
        saved_file = open("savedProductLinks.txt", "r")
        line = saved_file.readline()

        while line != NULL:
            saved_links.append(line)
            line = saved_file.readline()

    else:
        print("Options List")
        print("1 : Add Item to Track")
        print("2 : Save List to Text File")
        print("3 : Quit Program")

        choice = input("What would you like to do?")

        if choice == "1":
            addItem()
        elif choice == "2":
            saveList()
        elif choice == "3":
            exit()
        else:
            print("That is not a valid option")
