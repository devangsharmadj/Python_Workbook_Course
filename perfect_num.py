from functools import reduce
from time import time


# This is going to be a list that will store all the times
total_time = []


def main():
    # Getting user input with error handling
    while True:
        try:
            temp = int(input('Up to what number do you want to search for perfect numbers: '))
        except TypeError and ValueError:
            print('Please provide integer input')
        else:
            break
    # Calling the is_perfect function user number of times.
    for b in range(2, temp):
        is_perfect_v1(b)
    # Printing out rounded result
    print(f'It took {round(reduce(add, total_time, 0), 2)} seconds. ')


# This function is a function to be used with 'reduce'
def add(acc, i):
    return acc + i


# This decorator will record the time taken by each iteration
def performance(fn):
    def wrap_fn(*args, **kwargs):
        # Measuring time using the time func
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        total_time.append(t2 - t1)
    return wrap_fn


# This function will check if a number is a perfect number
@performance
def is_perfect_v1(number):
    factors = [1]
    for item in range(2, number):
        if number % item == 0 and item not in factors:
            temp = number/item
            factors.extend([item, temp])
    if number == reduce(add, factors, 0):
        print(number)
        return True
    else:
        return False


main()
