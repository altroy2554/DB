import pandas as pd

date = input("알고싶은 날을 입력하시오(2021-01-01)").split('-')

URL = f"https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={date[0]}{date[1]}{date[2]}"

date = pd.read_html(URL)

#print(date[0])

#print(date[0]) #0은 데이터
#print(date[1]) #data에 대한 정보 요약

df = date[0]

#print(df.head(1)) # *.head() = 5줄만 # *.head(n) = n줄만

#dataframe의 컬럼 추출
#df['컬럼이름']

mName = df['영화명']
#print(mName)

#print(mName.head())

#print(df[['영화명','평점','평점.1']])

#b = df.columns.values;print(b) # column들을 리스트로 만들어준다
#['순위' '영화명' '평점' '평점.1' '평점.2' '변동폭' '변동폭.1' 'Unnamed: 7']
a = df[['순위','영화명','평점.1']]
a.columns.values[2] = '평점'
#print(a)

#첫번쨰 행은 모두 NaN이다.
#dropna()
a = a.dropna(how='all')#모든것이 NaN이면 삭제하기
#print(a)

#print(len(a))#NaN인 행이 여러개 있고 중간에 다 삭제가 되어 48이 된다 10 -> 12

a['순위']=range(1,len(a)+1)
a.reset_index(drop=True, inplace= True)
#원본a도 변경 (inplace)

# 날짜 순위 영화명 평점
dat = URL.split('=')[-1]
a['날짜'] = f"{dat[:4]}-{dat[4:6]}-{dat[6:]}"
a = a[['날짜','순위','영화명','평점']]

print(a.head())
#
import random
def test1():
    a = random.randint(1,100)
    print(a)
    c['text'] = str(a)
    print(d['text'])

def test2():
    #d에 쓴 글씨를 가지고 와서 엔트리 f에 복사하기
    a = d.get()#d엔트리로부터 글자를 가지고 오기
    f.insert(0,a)

from tkinter import *
a = Tk()
b = Label(a,text="makit")
b.pack()
c = Button(a,text="Makit",command=test1)
c.pack()
d = Entry(a)#Entry는 입력받는 공간
d.pack()
f = Entry(a)
f.pack()
e = Button(a,text="가져오기",command = test2)
e.pack()


a.mainloop()#loop무한 이벤트 감시

