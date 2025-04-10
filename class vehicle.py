class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass  # Base method to be overridden


class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road 🚗"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying through the air ✈️"


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on water 🚢"


class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass  # Base method to be overridden


class Dog(Animal):
    def move(self):
        return f"{self.name} is running on four legs 🐕"


class Bird(Animal):
    def move(self):
        return f"{self.name} is flying with wings 🐦"


class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming with fins 🐠"


# Function to demonstrate polymorphism
def demonstrate_movement(entity):
    print(entity.move())


# Create instances of different vehicles and animals
entities = [
    Car("Toyota"),
    Plane("Boeing 747"),
    Boat("Sailboat"),
    Dog("Rex"),
    Bird("Sparrow"),
    Fish("Nemo")
]

# Demonstrate polymorphism
print("How different entities move:")
print("--------------------------")
for entity in entities:
    demonstrate_movement(entity)