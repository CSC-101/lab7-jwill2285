import convert
'''This function works by taking the input from the user asking for a float. when they give an input
the computer will ask if they want to continue adding. If they do it keeps going until they say done. All
of those inputs are put into a list that is later read in the function. The function takes the list and checks
if the input that is given is a float. If it is, the input is added to the list of floats. That is then
returned'''
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
