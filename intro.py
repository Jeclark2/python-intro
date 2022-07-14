if (3 > 2):
    print("3 is more than 2")
else:
    print("3 is not more than 2")

if (3 < 3):
    print("option 1")
elif (3 == 3):
    print("option 2")
else:
    print("got something else")

def print_stuff():
    print("a function is printing this")
    print("isn't that cool?!")

print_stuff()

if (3+7 > 4):
    print("3 plus 7 is more than 4")


def operation(a, b, c):
    return a**2 + b/4 - c

print(operation(3, 4, 2))
#this function has a return
def hello(n):
    return n*"hello"
#this function does not return anything

def rectangle_area(w,h):
    return w*h 
print(rectangle_area(15, 60))

def rectangle_perimeter(w,h):
    return w+w+h+h 
def rectange_info(width, height, X):
    if x=="a":
        return rectangle_area(width, height)
    elif x=="p":
        return rectangle_perimeter(width, height)
    else:return -1
print(rectangle_info(35, 500, "a"))
