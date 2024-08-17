# ====================================== Single Inheritance =======================================

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

# ====================================== Multiple Inheritance =======================================

class parent():
    def parentClass(self):
        print("This is a parent class")

class child_1(parent):
    def child1_class(self):
        print("This is a child class 1")

class child_2(parent):
    def child2_class(self):
        print("This is a child class 2")

# ========================================== Multilevel Inheritance ===================================================
class level_1():
    def level1_class(self):
        print("Level_1")
class level_2(level_1):
    def level2_class(self):
        print("Level_2")
class level_3(level_2):
    def level3_class(self):
        print("Level_3")

# ===================================================== Hierarchial Inheritance ===================================================
class hier_1():
    def hier1_(self):
        print("hierarchial 1")
class hier_2(hier_1):
    def hier2_(self):
        print("hierarchial 2")
class hier_3(hier_1):
    def hier3_(self):
        print("hierarchial 3")
# ===================================================== class calling ===================================================

def single_inheritance():
    Dog = dog("name", 56)
    Dog.printf()
    Dog.speak()

def multiple_inheritance():
    child1 = child_1()
    child2 = child_2()

    child1.parentClass()
    child2.child2_class()
    child1.child1_class()

def multilevel_inheritance():
    level3 = level_3()

    level3.level1_class()
    level3.level2_class()
    level3.level3_class()

def hierarchial_inheritance():
    hier2 = hier_2()
    hier3 = hier_3()

    hier2.hier1_()
    hier2.hier2_()

    hier3.hier1_()
    hier3.hier3_()
# ===================================================== Main Function ===================================================
def main():
    print("Single Inheritance".center(150, "-"))
    single_inheritance()
    print("Multiple Inheritance".center(150, "-"))
    multiple_inheritance()
    print("Multilevel Inheritance".center(150, "-"))
    multilevel_inheritance()
    print("Hierarchial Inheritance".center(150, "-"))
    hierarchial_inheritance()

# ===================================================== Main Function Call ===================================================
if __name__ == "__main__":
    main()