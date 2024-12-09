'''
Cecilia Adeniran
CS7 section D01
Programming Assignment 7
4/12/2024
'''
file = open("C:/Users/titi_/Downloads/A7dataSP24.data",'r')
d={'ANTH ':'Anthropology', 'CS   ':'Computer Science', 'BIOS ':'Biological Sciences','CHEM ':'Chemistry','FRENC':'French','POLYS':'Political Science','ZOO  ':'Zoology','BWRT ':'Business Writing','ARTH ':'Art History','MATH ':'Mathematics'}
print('Department','        ','Department Name')
print('-------------------------------')

for k in d:
    f= file.readline()
    abbr= f[20:25]
    name=f[0:19]
    print(abbr,'         ',name)
print('There are',len(d),'departments')
file = open("C:/Users/titi_/Downloads/A7dataSP24.data",'r')
Userinput = input('Enter Transaction: ')
while k in list(d):
    if Userinput[0]!= 'l' and Userinput[0] != 's' and Userinput[0] != 'a' and Userinput[0] !='c' and Userinput[0] != 'd' and Userinput[0] != 'x':
        print('ERROR: transaction does not exist')
        Userinput = input('Enter Transaction: ')
    while Userinput[0] =='s':
        Userinput = Userinput[1: ]
        Userinput = Userinput.lstrip()
        print(d.get(Userinput,'does not exist, might be missing spaces'))
        Userinput = input('Enter Transaction: ')
    while Userinput[0] =='d':
        Userinput = Userinput[1:]
        Userinput = Userinput.lstrip()
        try:
            del d[Userinput]
        except KeyError:
            print('does not exist, might be missing spaces')
        Userinput = input('Enter Transaction: ')
    while Userinput[0] =='a':
        Userinput = Userinput[1:]
        Userinput = Userinput.strip()
        if Userinput[0:4] in d:
            print('error already exists')
            Userinput = input('Enter Transaction: ')
        else:
            c = Userinput[5:]
            c = c.lstrip()
            d[Userinput[0:5]] = c
        Userinput = input('Enter Transaction: ')
    while Userinput[0] =='c':
        Userinput = Userinput[1:]
        Userinput = Userinput.strip()
        if Userinput[0:5] not in d:
            print('ERROR: does not exists')
        else:
            b = Userinput[0:5]
            c = Userinput[5:]
            c = c.lstrip()
            d.update({b:c})
        Userinput = input('Enter Transaction: ')
    while Userinput[0] == 'l':
        print('Department', '        ', 'Department Name')
        print('-------------------------------')
        for k in d:
            print(f'{k:<15}{d[k]}')
        print('There are', len(d), 'departments')
        Userinput = input('Enter Transaction: ')
    if Userinput[0] == 'x':
        print ('exiting program')
        break
file.close()
        













