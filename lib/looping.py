#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num >=1:
        print(num)
        num -= 1
    print("Happy New Year!")

#happy_new_year()

def square_integers(int_list):
    int_list = [int * int for int in int_list]
    return int_list

print(square_integers([2,3,5,6]))

# ALTERNATIVE LONGER SOLUTION BELOW

# def square_integers(int_list):
#     new_int_list = list()
#     for integer in int_list:
#         element = integer * integer
#         new_int_list.append(element)
#     return new_int_list

def fizzbuzz():
    num = 0
    while num < 100:
        num +=1
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()
