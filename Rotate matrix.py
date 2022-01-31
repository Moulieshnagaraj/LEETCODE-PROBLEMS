# Rotate the image.
'''
[[1,2,3],
 [4,5,6],
 [7,8,9]]

 output
 --------
[[7,4,1],
 [8,5,2],
 [9,6,3]]

'''
import numpy as np
myarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
def rotatearray(matrix, length):
    n=length
    for row in range(n//2): #here, 0 , 1
        first= row # 0
        last = n-row-1 # 2
        for i in range(first, last): # 0,2 --> 0,1
            # Saving the top first element
            top=matrix[row][i]
            # Moving the left bottom element to top first
            matrix[row][i] = matrix[-i-1][row]
            #Moving the right bottom element to left bottom
            matrix[-i-1][row]=matrix[-row-1][-i-1]
            # Moving the top right element to right bottom
            matrix[-row-1][-i-1] = matrix[i][-row-1]

            matrix[i][-row - 1] =top
    return matrix
print(rotatearray(myarray,len(myarray)))
