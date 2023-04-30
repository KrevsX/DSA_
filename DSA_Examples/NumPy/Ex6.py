#  Copyright (c) 2023. By.Kevin Alas
#  All rights reserved
#  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia
#  accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget
#  metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import numpy as np

array1d = np.array([1,2,3,4,5,6])
array2d = np.array([[1,2,3],[4,5,6]])
array3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(array1d)
print(array1d[0])
print(array1d[1])
print(array1d[-3])
print('----')
print(array2d)
print(array2d[0,0])
print(array2d[0,1])
print(array2d[1,-1])
print('----')
print(array3d[0,1,2])
print(array3d[1,1,-1])

