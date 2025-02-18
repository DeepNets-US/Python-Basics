"""
1. You should have at least four classes: the parent Animal class, and
then at least three child animal classes that inherit from Animal.
2. Each class should have a few attributes and at least one method
that models some behavior appropriate for a specific animal or all
animals—such as walking, running, eating, sleeping, and so on.
3. Keep it simple. Utilize inheritance. Make sure you output details
about the animals and their behaviors.
"""

class Animal:

    def __init__(self, name=None, legs=None):
        self.name = name
        self.legs = legs

    def speak(self, sound="hm?"):
        print(f"{self.name} says {sound}") if self.name is not None else print(sound)

    def sit(self):
        print(f"{self.name} is sitting") if self.name is not None else print("sitting")

    def stand(self):
        print(f"{self.name} is standing") if self.name is not None else print("standing")

class Dog(Animal):

    def bark(self):
        self.speak(sound="Woh Woh WOH..")

class Cow(Animal):
    def speak(self):
        super().speak(sound="UMmmmmmmm")

if __name__=='__main__':

    a = Dog(name="Tom")
    a.bark()

    c = Cow()
    c.speak()
