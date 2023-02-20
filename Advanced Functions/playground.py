
# unlimited positional arguments -- the positions in which you pass the variables are of
# some importance. The '*" operator collects all of the parameters into a tuple.
def add(*args):
    return sum([n for n in args])

print(add(5,6,7,10))

# Refer to your parameters by name in your function:
# Keyword arguments values can be referred to by the key passed in the functions call
def calculate(n,**kwargs):
    # print(type(kwargs), kwargs)
    items = {(k,v) for k,v in kwargs.items()}
    # print(items)
    n += kwargs['add']
    n *= kwargs['multiply']
    # print(n)

calculate(5, add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']

my_car = Car(make='Nissan',model='GT-R')
print(my_car.model)

def test(*args):
    print(type(args))

test(1,23,5,6)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)