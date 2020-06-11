import numpy as np

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def recursion(list, num):
    if list[0] == num:
        print('True')
    
    if len(list) == 0:
        print('False')

    else:
        return recursion(list[1:0], num)

recursion(list, 3)

# will have to watch the lecture to figure this out.