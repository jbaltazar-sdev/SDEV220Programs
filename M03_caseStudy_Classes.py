'''
Write a Python app that has the following classes:

    A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
    A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
        year
        make
        model
        doors (2 or 4)
        roof (solid or sun roof).
    Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
    The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
    The app will then output the data in an easy-to-read and understandable format, such as this:
      Vehicle type: car
      Year: 2022
      Make: Toyota
      Model: Corolla
      Number of doors: 4
      Type of roof: sun roof

'''

class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type = vehicle_type
        
class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        
        if doors in (2, 4):
            self.doors = doors
        else:
            raise ValueError("Door must be 2 or 4")
        
        if roof.lower() in ("solid", "sunroof"):
            self.roof = roof
        else:
            raise ValueError("Roof must be 'solid' or 'sunroof'.")
    
    def __str__(self):
        return (
            f"Vehicle type: {self.vehicle_type}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Doors: {self.doors}\n"
            f"Roof: {self.roof}"
        )   
            
year = int(input("Enter the year of your automobile: "))
make = input("Enter the make of your automobile: ")
model = input("Enter the model of your automobile: ")
doors = int(input("Enter if your automobile has 2 or 4 doors: "))
roof = input("Enter the roof type for your automobile: ")
car = Automobile('car', year, make, model, doors, roof)
print(car)
