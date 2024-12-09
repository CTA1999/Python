'''
Cecilia Adeniran
PA3
cs7 - section D01:
2/17/24
'''

import math

print('**************** Part 1 *************')
counter = 1
while (counter <=12):
        print(counter)
        print('the square root of', counter, 'is', math.sqrt(counter))
        print('the square of', counter, 'is', counter ** 2)
        counter = counter + 1
else:
    counter = 14
    while(counter <=15):
        print(counter)
        print('the square root of', counter, 'is', math.sqrt(counter))
        print('the square of', counter, 'is', counter ** 2)
        counter = counter + 1


print('********* Part 2 *********')
sum = 0
counter = 30
while( counter <=40):
       sum = sum + counter
       counter = counter + 1
       print (sum)

print('********** section 3 **********')
higher = (int(input('enter higher bound of integers: ')))
lower = (int(input('enter lower bound of  integer: ')))
sum = 0
counter = lower
while( counter <= higher):
       sum = sum + counter
       counter = counter + 1
       print (sum)

print('********** section 4 **********')
name = input(' enter the name Dagny, Hank, or Francisco')
while (name !='Dagny' and name!='Hank' and name!='Francisco'):
       print('Error, try again')
       name = input(' enter the name Dagny, Hank, or Francisco')
else:
       print('Success')


print('********** section 5 **********')

number = int()
while number >= 0:
    number = int(input("Enter a number: "))
    if number < 0:
        print('Finished')
    elif number == 1:
        print("Abigail")
    elif number == 2:
        print("Bobby")
    elif number == 3:
        print("Charmaine")
    elif (number !=1 and number !=2 and number !=3 and number >0):
        print("Error!")

print('********** Section 6 **********')
name = input('Enter a name: ')
while(name !='Frank' and name != 'Betty'):
    print('Try Again')
    name = input('Enter a name: ')
else:
    print('You did well!')

























