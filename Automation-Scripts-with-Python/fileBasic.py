import csv, json
with open ("csvfile.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    for row in reader:
        print(row)

with open ("jsonfile.json", "r") as jsonfile:
    data = json.load(jsonfile)

j=0

for i in data:
    print(i["fname"], i["lname"], i["age"], i["hobbies"])
    j+=1