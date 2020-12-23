from typing import TextIO, List

NUMBER = '1234567890'
def check_password(file: TextIO) -> bool:
    """
    
    >>> file = open("day2_input.txt")
    >>> check_password(file)
    """
    
    correct = 0
    for line in file:
        lst = line.strip().split(':')
        count = 0
        for item in lst:
            item = item.strip()
            if not(item.isalpha()):
                lst1 = item.split('-')
                start = int(lst1[0])
                end_lst = lst1[1].split()
                end = int(end_lst[0])
                letter = end_lst[1]
            if item.isalpha():
                count = item.count(letter)
            if start <= count <= end:
                correct = correct + 1
    return correct
                

#file = open("day2_input.txt")
#check_password(file)                

def check_position(file: TextIO) -> bool:
    
    correct = 0
    for line in file:
        lst = line.strip().split(':')
        for item in lst:
            item = item.strip()
            if not(item.isalpha()):
                lst1 = item.split('-')
                start = int(lst1[0])
                end_lst = lst1[1].split()
                end = int(end_lst[0])
                letter = end_lst[1]
            if item.isalpha() and len(item) > (end - 1): 
                if (item[start - 1] == letter) and not (item[end - 1] == letter):
                    correct = correct + 1
                elif (item[end - 1] == letter) and not (item[start - 1] == letter):
                    correct = correct + 1
    return correct    

