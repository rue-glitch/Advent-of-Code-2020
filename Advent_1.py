from typing import TextIO, List

def get_product(file: TextIO) -> int:
    """ Returns the product of two numbers from a file if and only if 
    they both sum up to 2020.
    
    >>> file = open("input.txt")
    >>> get_product(file)
    926464
    """

    lst = file.readlines()
    num = []
    for item in lst:
        item = int(item.strip())
        num.append(item)
    
    for number in num:
        for num2 in num:
            if number + num2 == 2020:
                return number * num2


def triple_product(file: TextIO) -> int:
    """Returns the product of three numbers from a file if and only if 
    they sum up to 2020.
    >>> file = open("input.txt")
    >>> triple_product(file)
    926464
    """
    
    lst = file.readlines()
    num = []
    for item in lst:
        item = int(item.strip())
        num.append(item)
    
    for number in num:
        for num2 in num:
            for num3 in num:
                if number + num2 + num3 == 2020:
                    return number * num2 * num3
    