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

print("Example 1")
first_numpy = np.array([1,2,3,4,5,6,7,8,9])
print(first_numpy)
print("Example 2")
arraywithzeros = np.zeros((3,3))
print(arraywithzeros)
print("Example 3")
arrayones = np.ones((3,3))
print(arrayones)
print("Example 4")
arrayempty = np.empty((2,3))
print(arrayempty)
print("Example 5")
nparrange = np.arange(12)
print(nparrange)
print("Reshape Example 5")
print(nparrange.reshape((3,4)))
print("Example 6")
np_linspace = np.linspace(1,6,5)
print(np_linspace)
print("Example 7")
oneD_array = np.arange(15)
print(oneD_array)
print("Convert 2D Example 7")
twoD = oneD_array.reshape((3,5))
print(twoD)
print("Example 8")
threeD = np.arange(27).reshape(3, 3,3)
print(threeD)
