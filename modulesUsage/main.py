import hi as greet

name = input("Enter the name: ")

greet.say_hi(name)
greet.come_again(name)
greet.modules()
greet.new_line()

# decision=input("Odd Even ??")

if(int(input("odd even ?"))==1):
    try:
        num = int(input("Enter the number: "))
        print(greet.oddEven(num))
    except:
        print("Enter the number.....")
        greet.try_again()
else:
    greet.thank_you(name)