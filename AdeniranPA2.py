'''
PA2
CS7
2/11/24
Cecilia Adeniran
'''
import math
import random


#Part 1. Travel mileage

gas = float(input('Enter the cost of the tank of gas:  '))
miles = float(input('Enter the number of miles driven:   '))
print('Cost of gas:       $',   format(gas,'.2f'))
print('Miles driven:       ', format(miles,'.2f'))
cpm = gas/miles
print('Cost per mile:     $',format(cpm,'6.2f'))

#Part 2. Interest Calculations

print('Enter principal')
p = float(input(''))
print('Enter Interest Rate')
i = float(input(''))
print('For a loan of                $',format(p,'10.2f'))
print('With a rate of               ',format(i,'11.2f'),'%')
ica = (p*i)/100
print('Interest compounded annually $',format(ica,'10.2f'))
ye = ica + p
print('YE balance                   $',format(ye,'10.2f'))
icd = (p*(1+((i/100)/365))**365)-p
print('interest compounded daily    $',format(icd,'10.2f'))
fye = p+icd
print('YE balance                   $',format(fye,'10.2f'))

#Part 3. Screen Size Calculations
a = float(input('Enter the height of the screen in inches: '))
b = float(input('Enter the width of the  screen in inches: '))
c= math.sqrt(a**2 +b**2)
print('The size of the display screen is: ',format(c,'.2f'))

#Part 4. Las Vegas Dice Game
a = random.randint(1,6)
b = random.randint(1,6)
print(a,',',b)
sum=a+b
if(sum == 7 or sum == 11):
    print('Winner')
else:
    if (sum == 2 or sum == 3 or sum == 12):
        print('Loser')
    else:
        print('point made is', a+b)
        print('Roll again')
    c = random.randint(1,6)
    d = random.randint(1,6)
    print(c,',',d)
    sum2=c+d
    if(sum2 == sum):
        print('Winner')
    else:
        print('Loser')

