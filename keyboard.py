import convert

def gather_numbers()->list[float]:
    list = []
    check = 'yes'
    while check == 'yes':
        line = input("Enter a float: ")
        if convert.str_to_float(line):
            list.append(line)
        check = input("Continue? (yes/done) ")
    return list


if __name__ == '__main__':
    print("The list of numbers is: ", gather_numbers())
