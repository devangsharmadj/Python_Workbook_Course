license = input('License number: ')
# Verifying old and new license numbers
if len(license) != 6 and len(license) != 7:
    print('Invalid license plate!')
for char in range(len(license)):
    if license[0].isupper() and license[1].isupper() and license[2].isupper() and license[3].isnumeric()  \
            and license[4].isnumeric() and license[5].isnumeric():
        print('Your license plate is an old fashioned one!')
        break
    elif license[0].isnumeric() and license[1].isnumeric() and license[2].isnumeric() and license[3].isnumeric()  and \
            license[4].isupper() and license[5].isupper() and license[6].isupper():
        print('Your license plate is a new fashioned one!')
        break
    else:
        print('Invalid license plate!')
        break
