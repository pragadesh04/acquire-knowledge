import csv, json
import os
import pyautogui as pg
import time as t
import requests
import json

decision = int(input("Choose the decision\n1 to read\n2 To write\n3 To sys commands\n4 PyautoGui Scripts"))

if decision == 1:
    with open ("csvfile.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")

        for row in reader:
            print(row)

    with open ("jsonfile.json", "r") as jsonfile:
        data = json.load(jsonfile)

    j=0

    print(data)
    for i in data:
        print(i["fname"], i["lname"], i["age"], i["hobbies"])
        j+=1

if decision == 2:

    decision_2 = int,input("enter\n1 Normal\n2 CSV\n")

    if decision_2 == 1:
        file = open("writeFile.txt", "w")
        lines = ["Hi guys", "How are you", "I am fine"]

        for i in lines:
            file.write(i + "\n")
    if decision_2 == 2:
        my_list = [1, 2, 3, 4, 5]
        with open('output.csv', 'w', newline='') as csvfile:
            mywriter = csv.writer(csvfile, delimiter=',')
            mywriter.writerow(my_list)

    print("Data written to output.csv")

if decision == 3:
    
    print(os.system('dir')) #this lists all the file in the directory

if decision == 4:
    sc_w, sc_h = pg.size()

    print(pg.position())
    pg.moveTo(825, 398, duration=0.2)
    print(sc_w, sc_h)
    t.sleep(5)

    pg.typewrite("""
    [
    {
        "id" : 1,
        "fname" : "John",
        "lname" : "Luther",
        "age" : 25,
        "hobbies":[
            "running", "dancing", "painting"
        ]   
    },
    {
        "id" : 2,
        "fname" : "John",
        "lname" : "Cartel",
        "age" : 34,
        "hobbies":[
            "Working", "GoingWork", "Gym"
        ]
    }
]
""",interval=0.05)
    
if decision == 5:

    url = 'https://dummyjson.com/products'
    
    # Get data from API
    response = requests.get(url)
    
    # load json data
    data = json.loads(response.text)
    for item in data["products"]:
        print(item["title"])
        print(item["price"] , "$")
        print(item["description"])
        print(item["category"])
        print(item["discountPercentage"])
        print(item["warrantyInformation"])
        print(item["shippingInformation"])
        print(item["availabilityStatus"])
        print()