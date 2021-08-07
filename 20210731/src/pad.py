'''
import pandas as pd

#          col1  col2  col3 ...(열)
# row1
# row2
# row3
# .
# .
# (행)

#인덱스 번호가 0부터 자동으로 주어진다
#a = pd.read_csv('../bin/countries.csv')

#첫번쨰 열을 인덱스로 사용
a = pd.read_csv('../bin/countries.csv', index_col=0)

print(a['area'])                          #1차원
print(a[['area']])                       #2차원
print(a[['area','capital']])        #2차원

b = a.head() #a data frame의 위에서 5줄만 b로 가져가기
print(b)

c=a[:3] #a의 0,1,2 3줄만 c로 가져가기
print(c)

d = a.tail() #a에서 마지막 5줄만 d로 가져가기
print(d)

# a[3:10] / 3번째 줄에서 9번째 줄까지 출력 또는 가져간다

'''
'''
   country      area     capital  population
KR   Korea     98480       Seoul    51780579
US     USA   9629091  Washington   331002825
JP   Japan    377835       Tokyo   125960000
CN   China   9596960     Beijing  1439323688
RU  Russia  17100000      Moscow   146748600
'''
'''
#위와 같은 data frame을 a라고 함
#kR행 정보만을 가져오기
b = a.loc['KR']
print(b)
'''
'''^code
country          Korea
area             98480
capital          Seoul
population    51780579
Name: KR, dtype: object
'''
'''

#data frame 은 열로 구성된 정보

print(a['population'][:3])
'''
'''
KR     51780579
US    331002825
JP    125960000
Name: population, dtype: int64
'''
'''

print(a.loc["US","capital"])
print(a.loc["US"])

print(a['capital'])
'''
'''
KR         Seoul
US    Washington
JP         Tokyo
CN       Beijing
RU        Moscow
Name: capital, dtype: object
'''
'''

print(a['capital'].loc['US'])
'''
'''
Washington
'''
'''

# csv로부터 읽어와서 a라는 data frame을 만듬
# 인구밀도 열 column을 추가

a['density'] = a['population']/a['area']
print(a)
'''
'''
       country      area         capital       population      density
KR   Korea      98480             Seoul      51780579    525.797918
US     USA   9629091  Washington    331002825    34.375293
JP    Japan     377835            Tokyo    125960000  333.373033
CN   China  9596960           Beijing  1439323688  149.977044
RU  Russia  17100000        Moscow    146748600       8.581789
'''
'''

print(a.describe())

## 표준편차 standart deviation
################################

print(a.count())
print(f"면적정보의 개수 : {a['area'].count()}")
print(a[['area','density']].count())

print(a[['area','density']].mean())#mean : 평균
'''

import pandas as pd

w = pd.read_csv("../bin/weather.csv",encoding = 'CP949')#한글 깨짐 방지
print(w)

#최대 풍속이 10보다 큰 날은 몇일이나 있었을까
a = (w['최대 풍속(m/s)']>=10.0)
w['결과'] = a
print(w)
cnt = 0;cnt2=0
for i in w['결과']:
    if i == True:
        cnt+=1
    else:
        cnt2+=1
print(cnt)
print(f'{round(cnt/(cnt+cnt2)*100,1)}%')

#데이터는 언제나 결측치 ./ 측정되지 않은 데이터가 있을 수 있음.

#결손값을 표현하는 방법
#공백보다는 NaN(Not A Number)으로 표시 또는 NA(Not Available)
missing = w[w['평균 풍속(m/s)'].isna()]
print(missing)

#NaN 값이 존재하는지 체크하는것이 중요하고
#NaN 값이 있다면 완벽한 데이터를 위해서 결손값을 넣어준다
#0또는 모든 데이터의 평균 값으로 넣어주는것처럼 후처리를 한다
#또는 값을 넣어주지 않고 NaN이 있는 데이터는 삭제한다
#데이터를 없애는 방법

#df.dropna(axis=0,how='any',inplace=False)

# axis = 0 > 축 NaN이 포함도니 행을 모두 삭제
# axis = 1 > NaN이 포함된 열을 모두 삭제
# how > any와 all이 올 수 있다
# any는 결손데이터가 하나라도 포함되면 저거 대상
# all은 결손데이터가 전체여야 행/열 을 제거한다
#inplace는 True,False로 표현 가능
# inplace가 대치하다,바꿔치기 하다, 원본이 변경된다
# inplace가 False는 원본은 그대로 두고 NaN이 적용된 또다른 데이터가 적용된다

print(w)  #[3653 rows x 5 columns]
w2 = w.dropna(axis=0,how='any',inplace=False)
print(w2)#[3646 rows x 5 columns]

w.fillna(0,inplace=True) #원본까지 변경가능 NaN을 0으로 채우기

##############
import pandas as pd

a = pd.DataFrame({'col1':['val1','val2','val3'],
                                  'col2':['val1','val2','val3'],
                                  'col3':['val1','val2','val3']})
print(a)
