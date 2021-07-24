import csv
import matplotlib.pyplot as plt

f = open('./src/weather.csv')
data = csv.reader(f)
header = next(data)

monthlyWind = [0 for i in range(12)]
daysCounted= [0 for i in range(12)]

for row in data:
     month = int(row[0].split('-')[1])
     if row[3]!='':
          wind = float(row[3])
          monthlyWind[month-1] +=wind
          daysCounted[month-1]+=1

for i in range(12):
     monthlyWind[i]/=daysCounted[i]#업데이트(평균)

m = [i for i in range(1,12+1)]

plt.plot(m,monthlyWind,'blue')
plt.show()

f.close()
