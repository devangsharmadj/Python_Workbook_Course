import random
from functools import reduce
num_of_times = int(input('How many times would you like to flip the coin: '))
flip_row = int(input('How many times would you like to flip the coin in a row: '))
average = []
for i in range(num_of_times):
    flag = True
    # Temp will keep track of how many times it took to flip in a row
    temp = 0
    # counter will keep track of when the coin flip appeared flip_row number of times
    counter = 0
    n = random.choice([1, 2])
    # Loop to keep generating random numbers until counter = flip_row
    while counter != flip_row:
        # Loop below for heads
        if n % 2 == 0:
            counter = 0
            while n % 2 == 0 and flag:
                print('H ', end='')
                counter += 1
                temp += 1
                if counter == flip_row:
                    print(f' ({temp} flips)')
                    average.append(temp)
                    flag = False
                n = random.choice([1, 2])
        # Loop below for tails
        elif n % 2 == 1:
            counter = 0
            while n % 2 == 1 and flag:
                print('T ', end='')
                counter += 1
                temp += 1
                if counter == flip_row:
                    print(f' ({temp} flips)')
                    average.append(temp)
                    flag = False
                n = random.choice([1, 2])


def add(acc, item):
    return item + acc


sum1 = (reduce(add, average, 0)) / num_of_times
print(f'On average, {sum1} flips were needed.')
