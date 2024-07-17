file = open("data.txt", "r+")


def try_print(file):
    try:
        for lines in file:
            print(lines)
    except:
        print("Error reading the file...")

try_print(file)    

try:
    file.write("\n"+input("Enter the value: "))
except:
    print("Writing error....")
    
file.seek(0)
try_print(file)