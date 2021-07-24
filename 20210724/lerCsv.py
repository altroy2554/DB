import csv

f = open('./src/weather.csv')
data = csv.reader(f)
header = next(data)
# ^^^^^^^^^^^^^첫번째 줄은 설명하는 줄. 데이터가 아니므로 제거한다.
#[일시][평균기온][최대풍속][평균풍속]
max_ = float('-inf')#가장큰 값을 수하기 위해 가장 작은 값으로 초기화
for row in data:
     if row[2] == '':#데이터 누락 처리 
          wind = 0
     else:
          wind = float(row[2])
     if wind > max_:
          max_ = wind
          date_ = row[0]
print(max_,date_)
f.close()
