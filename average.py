from sys import exit

number = int(input('Enter a number: '))
if number == 0:
    print("The first number can't be zero")
    exit(1)
counter = 1
sum = number
average = number
while number != 0:
    number = int(input('Enter a number: '))
    if number == 0:
        continue
    sum += number
    counter += 1
    average = sum / counter


print(f'The average is {average}')
