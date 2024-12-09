'''
Cecilia Adeniran
A4
CS7 - Section D01
2/27
'''

import math

print('----------Part 1 ----------')
for i in range (1,11):
    print(i, math.sqrt(i),i**2)

print('---------- Part 2 ----------')
lower = int(input('Enter lower bound number: '))
upper = int(input('Enter upper bound of integers: '))
counter = lower
sum = 0
for i in range(lower,upper+1):
    sum = sum + counter
    counter += 1
    if (counter == upper+1):
     print('the sum of the range', lower,'-',upper,'is: ',sum)

print('---------- Part 3 ----------')
count = 0
s= input('Enter a string: ')
for i in range(len(s)):
        count+=1
print('this string has',count,'characters')

print('----------Part 4----------')
vowels = 0
s = input('Enter a string using only lower case letters: ')
for i in range(0,len(s)):
    if( s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] =='u'):
        vowels +=1
print('the number of vowels in this string are ',vowels)


print('---------- Part 5 ----------')
s=input('Enter your first name and last name with the names seperated by a blank: ')
x,y = s.split()
print('The number of characters in your first name are: ', len(x))
print('The number of characters in your last name are: ',len(y))

