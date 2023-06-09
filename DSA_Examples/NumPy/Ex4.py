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

x = np.array([i for i in range(10)])
print(x)

print(np.where(x % 2 == 0, 'even', 'odd'))

print("-----")

condilist = [x < 5, x > 5]
choiselist = [x ** 2, x ** 3]

print(np.select(condilist,choiselist, default=x))
