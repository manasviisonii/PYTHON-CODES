 #wap to create a rectangle class that consists of two methods area in class rectange and ccreate one more class whh consist the perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class inner:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
def main():
    length = int(input("enter length: "))
    width = int(input("enter width: "))

    rectangle = Rectangle(length, width)
    print("Area :", rectangle.area())

    perimeter = inner(length, width)
    print("Perimeter :", perimeter.perimeter())


if __name__ == "__main__":
    main()