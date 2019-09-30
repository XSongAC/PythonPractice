import random
answer = random.randint(1,10)
counter = 0
while True:
    counter += 1
    number = int(input('The number you guess: '))
    if number < answer:
        print('need bigger')
    elif number > answer:
        print('need smaller')
    else:
        print('You got the right number')
        break

print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

