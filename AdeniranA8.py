'''
Cecilia Adeniran
CS7 section D01
Programming Assignment 8
5/3/24
'''
import random
def coinflip():
    flip = random.randint(1, 2)
    if flip == 1:
        flip = 'heads'
    else:
        flip = 'tails'
    return flip

userinput = int(input('how may time do you want to flip the coins?'))
flip = 0
yes = 0
while flip < int(userinput):
    x = coinflip(),coinflip(),coinflip(),coinflip()
    if x[0] == 'heads' and x[1] =='heads' and x[2] =='heads' and x[3] =='heads':
        yes+=1
    flip+=1
print('# of flips with all 4 coins landing on heads: ', yes)
percentage = (yes/userinput)*100
print(format(percentage,'.2f'),'%')

import random

print('---------- Part 2 ----------')
def roll6():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    summ = die1 + die2
    return summ
d = {2: int(),3:int() ,4:int() ,5: int(),6:int() ,7: int(),8: int(), 9:int() ,10:int() ,11: int(),12: int()}

userinput = int(input('Enter # of rolls: '))
d[roll6()] = 0
count = 0
while count < int(userinput):
    roll = roll6()
    d[roll] +=1
    count+=1

for k in d:
    percentage = format(((d[k])/userinput)*100,'.2f')
    print('roll', f'{k:<2} {' occurrences '} {d[k]:<5} {percentage:<5} {'%'}')
