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

arr= np.array([[4,3,2],[10,1,0],[5,8,24]])
print(arr)
print("----")
print(np.amin(arr))
print("----")
print(np.amin(arr, axis=0))
print("----")
print(np.amin(arr, axis=1))
print("----")
print(np.amax(arr))
print("----")
print(np.amax(arr, axis=0))
print("----")
print(np.amax(arr, axis=1))
print("----")
print(np.median(arr))
print("----")
print(np.mean(arr))
print("----")
print(np.std(arr))
print("----")
print(np.var(arr))
print("----")
print(np.percentile(arr,50))
deg=np.array([0,30,45,60,90])
print(np.sin(deg*np.pi/180))
print("----")
print(np.cos(deg*np.pi/180))
print("----")
print(np.tan(deg*np.pi/180))
print("----")
arrT= np.array([0.1,0.8,-2.2,-9.87])
print(np.floor(arrT))
print("----")
print(np.ceil(arrT))


