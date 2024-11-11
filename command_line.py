import sys
import convert
'''This function takes the sys.argv that is called and checks if the value is a float. If it works
the float is added to the total. If the value is not a float the function will continue to go through
the list of inputs nad returns the total for the floats added up'''
def main()->float:
    total = 0.0
    for i in sys.argv:
        try:
            total += float(i)
        except ValueError:
            continue
    return total




if __name__ == '__main__':
    print(main())
    print(sys.argv)
