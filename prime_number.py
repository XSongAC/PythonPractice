from math import sqrt

num = int(input('The number you enter: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d is prime number' % num)
else:
    print('%d is Not a prime' % num)