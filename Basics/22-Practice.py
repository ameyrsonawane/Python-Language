'''class car():
    pass
Tata = car()
Honda = car()
Tata.Car_name = "Nexon"
Tata.Price = 12000000
Honda.Car_name = "City"
Honda.Price = 1500000
print(Tata.Car_name)
print(Tata.Price)
print(Honda.Car_name)
print(Honda.Price)'''

class car():
    def __init__(self):
        self.car_name = input("Enter Name-")
        self.price = int(input("Enter price-"))
        self.state = input("Name of State-")
        self.city = input("Name of City")
        print(self.car_name)
        print(self.price)
        print(self.state)
        print(self.city)
a = car()
