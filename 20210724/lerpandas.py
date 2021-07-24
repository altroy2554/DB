import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./src/countries.csv')
print(df)
df = pd.read_csv('./src/countries.csv',index_col =0)#자동 인덱스 대신 첫번째 column을 인덱스로 사용
print(df)

#     country     area        capital      population
#KR   Korea     98480       Seoul      51780579
#US     USA   9629091  Washington  331002825
#JP   Japan    377835       Tokyo     125960000
#CN   China   9596960     Beijing      1439323688
#RU  Russia  17100000   Moscow    146748600

w = pd.read_csv('./src/weather.csv',index_col = 0,encoding='CP949')
MaxWind = w['최대 풍속(m/s)']

print(df['capital'])                 #capital column을 가져오기
print(df[['country','capital']]) #country 와 capital column을 가져오기

a = df['population']

a.plot(kind = 'pie')#,color = ('b','orange','g','r','m'))
#pie 그래프는 색상 자동지정.

plt.show()
