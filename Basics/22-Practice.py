class movie:
    def d1 (self):
        print("Base Class")
class actor(movie):
    def d2 (self):
        print("1st Derived Class")
class director(actor):
    def d3 (self):
        print("2nd Derived Class")
obj=director()
obj.d1()
obj.d2()
obj.d3()

