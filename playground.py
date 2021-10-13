# *args: Positional Variable-Length Arguments
def add(*args):
    sum = 0
    for n in args:
        if not str(n).isdigit():
            return False
        else:
            sum += int(n)
    return sum


print(add(1, 4, 6, 7, 9))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multi"]
    print(n)
#     (2 + 3) * 9

calculate(2, add=3, multi=9)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        # get will return null if the key we're looking for doesn't exist
        # keeps the code from crashing
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
