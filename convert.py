#Task 1
from typing import Optional
'''the str_to_float function grabs a string value and will try to change it to a float
if it tries to change it to a float and this does not work because it is not a float
then it will return none thanks to the except part of the function'''
def str_to_float(val : str)->Optional[float]:
    try:
        return float(val)
    except ValueError:
        return None
