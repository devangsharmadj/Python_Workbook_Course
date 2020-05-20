verifier = input('String to be checked: ')
split_verifier = verifier.split()
str_verifier = ''
for char in split_verifier:
    str_verifier += f'{char}'
j = len(str_verifier)
for i in range(len(str_verifier)):
    if str_verifier[i] == str_verifier[j - 1 - i]:
        continue
    else:
        print('Not a palindrome!')
        exit(1)
print('Palindrome!')
