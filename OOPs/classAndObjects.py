class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printf(self):
        print(f"{self.name} {self.age}")

def main():
    animalObj = animal("Dog", 12)

    animalObj.printf()

if __name__ == "__main__":
    main()