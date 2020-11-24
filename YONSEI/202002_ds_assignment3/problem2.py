import numpy as np

'''
Problem 2
2-1
|       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|
| **1** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| **2** | 2 | 4 | 6 | 8 |10 |12 |14 |16 |18 |
| **3** | 3 | 0 | 3 | 0 | 3 | 0 | 3 | 0 | 3 |
| **4** | 4 | 2 | 6 | 4 | 8 | 6 |10 | 8 |12 |
| **5** | 5 | 4 | 9 | 8 |13 |12 |17 |16 |21 |
| **6** | 6 | 0 | 6 | 0 | 6 | 0 | 6 | 0 | 6 |

2-2
|       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|
| **1** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| **2** | 2 | 4 | 6 | 8 | 0 | 2 | 4 | 6 | 8 |
| **3** | 3 | 0 | 3 | 0 | 3 | 0 | 3 | 0 | 3 |
| **4** | 4 | 2 | 6 | 4 | 0 | 4 | 2 | 6 | 4 |
| **5** | 5 | 4 | 9 | 8 | 5 |10 | 9 |14 |13 |
| **6** | 6 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 |

'''

#점화식 
#n=1 -> T(w,h) = w*h - (w/w1 * h/h1)*w1*h1

def problem2(width, height, desired_size):
    table = np.full((width,height),-1)

    '''if len(desired_size) == 1:
        return width*height - ((int(width/desired_size[0][0])
            *int(height/desired_size[0][1]))
            *desired_size[0][0]
            *desired_size[0][1])'''

    for i in range(len(table[0])): # column
        for j in range(len(table)): # row
            print(table[j][i],end='')
        print()
    

desired_size = [(2,3)]
print(problem2(9,6,desired_size))