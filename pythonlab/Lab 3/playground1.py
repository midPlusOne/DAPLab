class Polygon:
    #Constructor initializes the values
    def __init__(self, sides):
        self.side = sides
        self.sides = [0 for i in range(sides)]
    #inputSide takes the side values
    def inputSide(self):
        for i in range(self.side):
            self.sides[i] = float(input(f"Enter side {i + 1}: "))
    #dispSide displays the value
    def dispSide(self):
        for i in range(self.side):
            print(f"Side {i + 1}: {self.sides[i]}")

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    #Calculates area of traingle using semiperimeter method
    def findArea(self):
        a, b, c = self.sides

        s = (a + b + c) / 2

        area = (s * (s - a) * (s - b) * (s - c))**0.5
        print(area)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def findArea(self):
        l,b = self.sides

        area = l * b
        print(area)

print("------ Triangle ------")
t = Triangle()
t.inputSide()
t.dispSide()
t.findArea()

print("------ Rectangle ------")
r = Rectangle()
r.inputSide()
r.dispSide()
r.findArea()