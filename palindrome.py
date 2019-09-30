"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: Xiwen
Date: 2019-09-24
"""
num = int(input("Please enter a positive number: "))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
    print("Here temp is: " , temp, "And num2 is : ", num2)
if num == num2:
    print("%d is a palindrome number" %num)
else:
    print("%d Not a palindrome number" %num)