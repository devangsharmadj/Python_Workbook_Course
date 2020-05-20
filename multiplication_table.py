table = int(input('How many rows and columns would you like: '))

counter = 1
for i in range(1, table + 1):
    if i == 1:
        print('\t', end='')
        for temp1 in range(1, table + 1):
            print(f'\t{temp1}', end='')
        print()
    else:
        print(f'\t{i}', end='')
    for j in range(1, table + 1):
        if i == 1 and counter == 1:
            print('\t1', end='')
            counter += 1
        print(f'\t{i * j}', end='')

    print()
