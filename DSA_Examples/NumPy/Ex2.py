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
np.array([1,2,3,4,5])
print(np.array([1,2,3,4,5]))

print("Example 2")
numpy_array = np.array([x for x in range(1,10)])
print(numpy_array)

#Reshape Example 2

print(numpy_array.reshape(3,3))

print("Example 3")
numpy_arraytwo = np.array([x for x in range(1,13)])
print(numpy_arraytwo)
#Reshape with 2Versions in Example 3
print(numpy_arraytwo.reshape(2,2,3))
print("----")
print(numpy_arraytwo.reshape(3,2,2))
print("----")
print(numpy_arraytwo.reshape(2,2,-1))
print("----")
numpy_three = numpy_arraytwo.reshape(3,2,2)
print(numpy_three)
print("----")
print(numpy_three.reshape(-1))
