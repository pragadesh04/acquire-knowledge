""" Given the names and grades for each student in a class of N students, store them in a
nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade. order their names
alphabetically and print each name on a new line.
Example
chi" , 20.0], ["beta" , 50.0], alpha" , 50.0]]
records =
The ordered list of scores is [20.0, 50.0]. so the second lowest score is 50.0. There are
two students with that score: ["beta" , alpha"]. Ordered alphabetically. the names are
printed as: """

n,i, records = int(input()),0, []
while i<n:
    name = input()
    score = input()
    records.append([name,score])
    i+=1

records.sort(key=lambda X: (X[1], X[0]))
print(records)

first = records[0][1]

for record in records:
    if record[1] > first:
        second = record[1]
        break
        
for record in records:
    if record[1] == second:
        print(record[0])
# print(records)