'''
Cecilia Adeniran
CS7 section D01
Programming Assignment 6
3/26/2024
'''
import statistics
file = open("C:/Users/titi_/Downloads/A6F24data.txt",'r')
movies = []
genre=[]
rating = []
f= file.readline()
rater = f[0:10]
print('Rater: ',f[0:10],f[10:25])
age = int(f[25:27])
if age >= 78:
    gen = 'Silent'
elif age >=59:
    gen = 'Baby Boomer'
elif age >= 43:
    gen = 'Gen X'
elif age >= 27:
    gen = 'Millenial'
elif gen >= 4:
    gen = 'Gen Z'
else:
    gen = 'Alpha'
age = print('Age of rater: ',age,',', gen)
while (len(f) != 0):
    f = f.rstrip()
    movies.append(f[0:20])
    genre.append(f[21])
    rating.append(f[20])
    f = file.readline()
del rating[0]
del movies[0]
del genre[0]
for i in range (0,len(genre)):
    if genre[i] =='S':
        genre[i] ='Sci-fi'
    elif genre[i]== 'C':
        genre[i] = 'Comedy'
    elif genre[i] =='R':
        genre[i] = 'Rom-com'
    elif genre[i] =='A':
        genre[i] = 'Action'
    elif genre[i] == 'H':
        genre[i] = 'Horror'
    elif genre[i] == 'D':
        genre[i] = 'Drama'
rater = rater.rstrip()
print(rater,'rated',len(movies),'movies:')
for i in range (0,len(movies)):
    print('Movie:',movies[i],f'{genre[i]:<10} {'Rating:'} {rating[i]}')
num = [int(i) for i in rating]
print('Average rating: ',format(statistics.mean(num),'.2f'))
file.close()






