import numpy as np

class IncorrectArraySize():
    array = list(arr.shape)
    if array[0] != array[1]:
        raise ValueError('Input should be a square matrix')    

arr = np.array([[1,2,3,7],
                [4,5,6,8],
                [5,8,9,7],
                [4,3,5,2]])
        
try:
    hold = []
    
    for i in range(len(arr)+1):
        hold.append(-i)
    
    hold_left = [i for i in hold if i<0]
    hold_right = [abs(i) for i in hold if i+len(arr)!=0]
    total_right = 0
    total_left = 0
    right = []
    left = []
    
    for x,y in enumerate(hold_right):
        num = arr[x][y]
        right.append(num)
        total_right+=num
        
    for i,j in enumerate(hold_left):
        num = arr[i][j]
        left.append(num)
        total_left+=num
    
    total = total_right + total_left
    print('The sum of the diagonals is {}'.format(total))
    
except IncorrectArraySize:
    print('Error')


