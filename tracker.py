import requests
import os

path = os.getcwd()
dir_list = os.listdir(path)
saved_links = []

'''if "savedProductLinks.txt" in dir_list:
    saved_file = open("savedProductLinks.txt", "r")
    line = saved_file.readline()

    while line != None:
        saved_links.append(line)
        line = saved_file.readline()
'''


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
    print("6 : Quit Program")

    choice = input("What would you like to do?\n")

    if choice == "1":
        productName = input("Enter the product name:\n")
        URL = input("Enter the link of the product:\n")
        saved_links.append([productName, URL])
        print("This product will be tracked\n")
    elif choice == "2":
        saveList()
    elif choice == "3":
        removeName = input("Enter the name of the product:\n")
        removeItem(removeName)
    elif choice == "4":
        track()
    elif choice == "5":
        printList()
    elif choice == "6":
        quit()
    else:
        print("That is not a valid option")
