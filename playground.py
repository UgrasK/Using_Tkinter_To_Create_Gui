# define unlimited arguments on function with *args (args can be any name like *numbers, *letters etc.)
def add(*args):
    sum_num = 0
    for num in args:
        sum_num += num
    return sum_num


print(add(3, 5, 6, 8))

# define unlimited keyword arguments on function with **kwargs (kwargs can be any name)
class Car:

    def __init__(self, **kw):
        self.brand = kw.get("brand")
        self.model = kw.get("GT-R")


my_car = Car(brand="Porsche")
print(my_car.brand)