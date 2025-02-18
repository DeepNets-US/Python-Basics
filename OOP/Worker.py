from Employee import Employee

class Worker(Employee):

    def __init__(self, part_time=True, **kwarg):
        super().__init__(**kwarg)
        self.part_time = part_time

    def hire(self):
        self.part_time = False
        print(f"Congratulations {self.name}, you are noy hired!")
   
   # Overriding
    def rest(self, n):
        print("Workers can't rest!")

if __name__=='__main__':

    a = Worker(
            name="Alex",
            age=78,
            department="IT"
        )
    print(a.work())
    print(a.rest(2))
    print(a.hire())
    print(a)
