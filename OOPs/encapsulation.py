class amount:
    def __init__(self, name, salary, expense):
        self.name= name #public can acces anywhere
        self.__salary = salary #private only within this class
        self.expense = expense 
        
    def show(self):
        print(self.name, self.__salary, self.expense)
        
    def give(self):
        return self.salary
    

amounts = amount("pragadesh", 40000, 25000)

amounts.show()
print(amounts.give()) #returns error because  the salary is private