from termcolor import colored 


def calender():
    day_num = 1
    print(colored(" Mon  Tue  Wed  Thru  Fri  Sat  Sun ","red"))
    for week in range(5):
        for day in range(7):
            print(f"{day_num:>4}", end=" ")
            day_num += 1
            if day_num > 31:
                break; 
        print("\n")
calender()

from termcolor import colored 
import random
import time
import math 

def pick(lst):
    return lst[random.randint(0, len(lst)-1)]

def mod_pick(lst, j):
    return lst[j % random.randint(1, len(chars))]

colors = [
        "blue",
        "cyan",
        "white",
]

chars = ['A','/','@','B']

def generate_mod():
    while(True):
        for i in range(100):
            for j in range(100):
                print(colored(mod_pick(chars, j), pick(colors)), end='')
        print()
        time.sleep(0.1)


generate_mod()


def sum_tuple(tuple):
    total = 0
    for i in range(len(tuple)):
        total = total + tuple[i]
    return total

    tup = (8, 7, 6, 5, 4)
    print(sum_tuple(tup))