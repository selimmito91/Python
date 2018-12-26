
class car:

    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __str__(self):
        return f'a {self.color} car'


my_car = car('red', 100)
print(str(my_car))