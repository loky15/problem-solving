#SUM OF EVEN FIBONACCI NUMBERS UNDER A RANGE
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        s = 0
        a , b = 1 , 2
        for i in range(n+1):
            c = a + b
            if (c >= n):
                break
            if c % 2 == 0:
                s += c
            a = b
            b = c
        print(s+2)
