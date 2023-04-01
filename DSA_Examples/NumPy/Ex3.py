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

A=np.array([[1,2,1],[2,2,3]])
B=np.array([3,4,5])
print(A)
print(B)
print("----")
print(np.add(A,B))
print("----")
print(np.subtract(B,A))
print("----")
print(np.multiply(A,B))
print("----")
print(np.divide(A,B))
print("----")
print(np.power(A,2))
print("----")
print(np.power(A,B))