"""
输出2~99之间的素数
Version: 0.1
Author: Xiwen
Date: 2019-09-24
"""

from math import sqrt
for num in range(2,100):
    is_prime = True
    for factor in range(2, int(sqrt(num))+1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")