from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    
    @abstractmethod
    def abstract_method2(self):
        pass

class methods(abstract):
    def __init__(self, name):
        self.name = name
        
    def abstract_method(self):
        return f"This is an abstract method_1 {self.name}"
    def abstract_method2(self):
        return f"this is an abstract method _ 2 {self.name}"
    
def main():
    ab = input()
    methods1 = methods(ab)  
    
    print(methods1.abstract_method())
    print(methods1.abstract_method2())
    
if __name__ == "__main__":
    main()