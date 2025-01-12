#!/usr/bin/env python3 

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for element in list:
        sum += element
    return sum

def prodl(list):
    global __counter    
    __counter += 1
    prod = 1
    for element in list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)