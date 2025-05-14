#*args:
def add(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(add(2,3,1,4,2,54))

#**kwargs:
def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(2, add=1, multiply=4))

#**kwargs with a CLASS:
class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')

my_car = Car()
my_car.make = 'Nissan'
my_car.seats = 2

print(my_car.make)
print(my_car.model)
