import time

class Employee: # Class Signature
    # Class's Body
    
    # Class Attributes
    company = "IBM"
    working = False

    # Take input during initialization
    def __init__(self, name, age, department):

        # Thes become class's attributes
        self.name = name
        self.age = age
        self.department = department
    
    # Define other methods
    def work(self):
        self.working = True
        print(f"{self.name} sent on work.")

    def is_working(self):
        return self.working

    def rest(self, n=10):
        self.working = False
        print(f"{self.name} resting for {n} sec.")
        time.sleep(n)
        self.working = True
        print(f"{self.name} is back on work.")
       
    def __repr__(self):
        return f'Employee({self.name}, {self.department})'
    

if __name__ == "__main__":
    alex = Employee("Alex",12,"IT")
    print(f"Alex's Company: {alex.company}")

    jack = Employee("Jack", 85,"IT")
    print(f"Jack's Company: {jack.company}")

