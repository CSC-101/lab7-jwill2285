import sys
import convert

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
