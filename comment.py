def main():
    input_file = input('File to be checked: ')
    output_file = input('Name of output file: ')
    in_file = open(input_file, 'r')
    out_file = open(output_file, 'w')
    while True:
        line = in_file.readline()
        if line == '':
            break
        if verifier(line) == '':
            temp = verifier(line).rstrip('\n')
            out_file.write(temp)
        else:
            out_file.write(verifier(line))


def verifier(line):
    checked_str = ''
    for char in line:
        if char == '#':
            return f'{checked_str}\n'
        else:
            checked_str += f'{char}'
    return checked_str


main()
