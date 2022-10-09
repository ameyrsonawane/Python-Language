# Class -> Class is a blueprint for creating an object. It is a logical structure with behaviour.
# Object -> Object is instance of class. Class contain methods,and we can access all those methods by creating object.

# __init__ -> init is constructor that automatically call to allocate the memory when new objet is created.
# All classes have init method.



class car():
  pass        # If we don't want to declare any details within the class put pass keyword.

Tata = car()
Honda = car()

Tata.model_name = "Nexon"
Tata.year = 2022
Tata.price = 1400000

Honda.model_name = "City"
Honda.year = 2020
Honda.price = 1200000

print("TATA->",Tata.model_name)
print("Manufacturing Year->",Tata.year)
print("On road price->",Tata.price)

print("HONDA->",Honda.model_name)
print("Manufacturing Year->",Honda.year)
print("On road price->",Honda.price)