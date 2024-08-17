class animal():
    def __init__ (self, name):
        self.name = name

    def speak(self):
        print("The animal makes a generic sound")

class dog(animal):
    def __init__ (self, name, age):
        super().__init__(name)
        self.age = age
    
    def printf(self):
        print(f"{self.name} {self.age}")

def main():
    Dog = dog("name", 56)

    Dog.printf()
    Dog.speak()

if __name__ == "__main__":
    main()