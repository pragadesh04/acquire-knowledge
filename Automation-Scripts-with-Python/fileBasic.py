import csv, json

decision = int(input("Choose the decision\n1 to read\n2 To write\n"))

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