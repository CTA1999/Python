'''
PA1
CS7 - Python
2/5/2024
Cecilia Adeniran
'''
days = float(input('Enter number of days worked last week: '))
hours = float(input('Enter number of hours you worked last week: '))
average = float(hours/days)
print('you averaged',average,'hours per day')

Fahrenheit = float(input('enter the temperature, in F: '))
Centigrade= float((Fahrenheit - 32) * 5/9)
print('That is',Centigrade,'in C')

ID = input('Enter your ID number: ')
FI = input('enter the first item type: ')
FC = float(input('Enter the first item cost: '))
Si = input('Enter the second item type: ')
Sc = float(input('Enter the second iem cost: '))
Ti = input('Enter the third item type: ')
Tc = float(input('Enter the third item cost: '))
print('-------------------receipt for',ID,'----------------------')
print( FI,FC)
print(Si,Sc)
print (Ti,Tc)
subtotal = FC + Sc + Tc
tax = .0926 * subtotal
print('subtotal', subtotal)
print('tax',tax)
total = tax + subtotal
print('total', total)
print('-----------------------------------------------------------------')

