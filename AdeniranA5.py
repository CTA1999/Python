'''
Cecilia Adeniran
CS7 section D01
Programming Assignment 5
3/8/2024
'''

import statistics
print('---------- Part 1 ----------')
tempList = []
temp= input("enter a temperature or stop: ")
while temp != 'stop' or temp!= 'STOP':
    tempList.append(temp)
    temp= input("enter a temperature or stop: ")
    if temp == 'stop' or temp == 'STOP':
        print('the temperatures you listed are: ')
        for i in range (0,len(tempList)):
            print(tempList[i])
        avg = (statistics.mean([float(i) for i in tempList]))
        print('the average temperature is: ',format(avg,'.2f'))
        break



print('---------- Part 2 ----------')
gradelist = []
hourlist = []
uinputlist=[]
hoursum = 0
sum = 0
uinput = input('enter a grade and number of hours or press calc to stop: ')
while input !='calc':
    gradelist.append(uinput[0])
    hourlist.append(uinput[2])
    uinputlist.append(uinput)
    if uinput!= 'calc' and int(uinput[2]) > 0:
        hoursum = hoursum + int(uinput[2])
        uinput = input('enter a grade and number of hours or press calc to stop: ')
        if uinput == 'calc' or uinput == 'CALC':
            print('the grades entered are:')
            for i in range(0, len(gradelist)):
                if gradelist[i] == 'a' or gradelist[i] == 'A':
                    a = (4 * int(hourlist[i]))
                    sum = sum + a
                elif (gradelist[i] == 'b' or gradelist[i] == 'B'):
                    b = (3 * int(hourlist[i]))
                    sum = sum + b
                elif (gradelist[i] == 'c' or gradelist[i] == 'C'):
                    c = (2 * int(hourlist[i]))
                    sum = sum + c
                elif (gradelist[i] == 'd' or gradelist[i] == 'D'):
                    d = (1 * int(hourlist[i]))
                    sum = sum + d
                elif (gradelist[i] == 'f' or gradelist[i] == 'F'):
                    f = (0 * int(hourlist[i]))
                    sum = sum + f
                print(uinputlist[i])
            print('your GPA is ',format(sum/hoursum,'.2f'))
            break































