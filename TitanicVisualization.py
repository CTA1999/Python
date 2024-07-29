
import matplotlib.pyplot as plt
import numpy as np
import random

print('---------- Part 2 --------')
survivedwomen = []
survivedmen = []
survivedchildren = []



file = open("C:/Users/titi_/Downloads/titanic_cleansed.csv",'r')
women= 0
men = 0
children = 0
count = 0
totalsurvived = 0
line = file.readline()
for line in file:
    line = line.split(',')
    if int(line[3]) == 1 and float(line[4]) >17 and int(line[1]) == 1:
        survivedwomen.append(line)
    if int(line[3]) == 0 and float(line[4]) > 17 and int(line[1]) == 1:
        survivedmen.append(line)
    if float(line[4]) <=17 and int(line[1]) == 1:
        survivedchildren.append(line)
        count+=1
    if int(line[3]) == 0 and float(line[4]) > 17:
        men+=1
    if int(line[3]) == 1 and float(line[4]) > 17:
        women+=1
    if float(line[4]) <= 17:
        children+=1
    if int(line[1]) == 1:
        totalsurvived +=1
print('total survived', totalsurvived)
wpercent = format((len(survivedwomen)/women) * 100, '.2f')
mpercent = format((len(survivedmen)/men) * 100, '.2f')
cpercent = format((len(survivedchildren)/children)* 100, '.2f')

print('total women', women, format((women/1309)*100,'.0f'), '%')
print('total men', men, format((men/1309)*100,'.0f'), '%')
print('total children', children, format((children/1309)*100,'.0f'), '%')

# pie chart for total passengers by group
y = np.array([30, 58, 12])
mylabels = ['Women'+ ' 30%', 'Men' + ' 58%', 'Children' + ' 12%']
plt.pie(y, labels = mylabels)
plt.title('Total Passangers by Group')
plt.show()



print('survived women/total women: ', len(survivedwomen), '/', women, wpercent, '%')
print('survived men/ total men: ', len(survivedmen), '/', men, mpercent, '%')
print('survived children/total children: ',len(survivedchildren), '/', children, cpercent, '%')
file.close()

# stacked graph
x = ['Women', 'Men', 'Children']
died = np.array([105, 631, 73])
survived = np.array([289, 130, 81])
plt.bar(x, survived, color = 'b')
plt.bar(x,died, bottom = survived, color = 'm' )
plt.legend(['survived', 'died'])
plt.show()







