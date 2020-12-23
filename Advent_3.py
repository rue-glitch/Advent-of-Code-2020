from typing import TextIO, List

def get_trees(file: TextIO, x: int, y:int) -> int:
    """
    >>> file = open("day3_input.txt")
    >>> get_trees(file)
    """
    
    counter_O = 0
    counter_X = 0
    count_line = 0
    line = file.readline()
    #lst = []
    num1 = x
    for line in file:
        line = line.strip()
        
        location = line*100
        
        if len(location) > num1:
            
            obstacle = location[num1]
        
            if obstacle == ".":
                counter_O = counter_O + 1
            if obstacle == "#":
                counter_X = counter_X + 1
                
        if y>1:
            (file.readline())*(y-1)
            
            #lst.append("okay")
        num1 = num1 + x
        count_line = count_line + 1
    return counter_X
            

       
def multiply_trees(file: TextIO) -> int:
    num1 = get_trees(file, 1, 1) #-> 79
    num2 = get_trees(file, 3, 1) #-> 234
    num3 = get_trees(file, 5, 1) #-> 72
    num4 = get_trees(file, 7, 1) #-> 91
    num5 = get_trees(file, 1, 2) #-> 35
    
    
    return num1, num2, num3, num4, num5