# +++++++++++++++++++++++++++++++++++++++++ method OverRiding +++++++++++++++++++++++++++++++++++++++
class animal:
    def sound():
        print("animal speaks")

class dog(animal):
    def sound():
        print("dog barks")

class cat():
    def sound():
        print("cat meows")


# +++++++++++++++++++++++++++++++++++++++++ method OverL0ading +++++++++++++++++++++++++++++++++++++++
class parent():
    def __init__(self, name, age =0):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")


# +++++++++++++++++++++++++++++++++++++++++ mains +++++++++++++++++++++++++++++++++++++++
def main():
    doggy = dog()
    catty = cat()
    animals = animal()

    print(" Method Overriding ".center(150, "0"))
    dog.sound()
    cat.sound()
    animal.sound()

    methodOL = parent("Pragadesh", 21)
    methodOL_1 = parent("pragadesh")

    print(" Method OverLoading ".center(150, "0"))
    methodOL.info()
    methodOL_1.info()

if __name__ == "__main__":
    main()