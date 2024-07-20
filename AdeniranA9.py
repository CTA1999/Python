
f = open("C:/Users/titi_/Downloads/titanic.csv",'r')
f2 = open("C:/Users/titi_/Downloads/titanic_cleansed.csv",'w')

f2.write('ID,survived,pclass,sex,age,sibsp,parch,fare,cabin,embarked\n')


age = []
fare = []

line = f.readline()
for line in f:
    line = line.split(',')
    del line[3:5], line[7]
    age.append(line[4])
    fare.append(line[7])

sum = 0
count = 0
for i in range(0,len(age)):
    if age[i] !='':
        age[i] = float(age[i])
        sum = sum + age[i]
        count +=1
averageage = str(format(sum/count,'.2f'))
for i in range (0,len(age)):
    if age[i] == '':
        age[i] = (averageage)
print(averageage)


#fare list
sum = 0
count = 0
for i in range(0,len(fare)):
    if fare[i] !='':
        fare[i] = float(fare[i])
        sum = sum + fare[i]
        count += 1
avgfare = (format(sum/count,'.2f'))
for i in range (0,len(fare)):
    if fare[i] == 0:
        fare[i] = float(avgfare)
print(avgfare)

f = open("C:/Users/titi_/Downloads/titanic.csv",'r')
line = f.readline()
for line in f:
    line = line.split(',')
    del line[3:5], line[7]
    age.append(line[4])
    fare.append(line[7])
    if line[3] == 'female':
        line[3] = '1'
    if line[3] == 'male':
        line[3] = '0'
    if line[4] == '':
        line[4] = averageage
    if line[7] == '':
        line[7] = avgfare
    if line[8] == '':
        line[8] = 'missing'
    if line[9] == '\n':
        line[9] = 'X' + '\n'
    line = ', '.join(line)
    print(line)
    f2.write(line)
f.close()
f2.close()





