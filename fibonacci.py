"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
Version: 0.1
Author: Xiwen
Date: 2019-09-26


a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=" ")
"""

"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
Version: 0.2
Author: Xiwen
Date: 2019-09-26
"""

# Program to display the Fibonacci sequence up to n-th term
# change this value for a different result
# nterm = 10


# uncomment to take input from the user
nterm = int(input("How many terms? "))
# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterm <= 0 :
    print("Please enter a positive integer")
elif nterm == 1:
    print("Fibonacci sequence upto:", nterm, ":")
    print(n1)
else :
    print("Fibonacci sequence upto:", nterm, ":")
    while count < nterm:
        print(n1, end=" , ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1