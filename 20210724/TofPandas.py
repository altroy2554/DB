import numpy as np
import pandas as pd
a =pd.Series([1,2,3])

nameSer = pd.Series(['name1','name2','name3'])
age        = pd.Series([10,20,30])
gender=pd.Series(['남','여','남'])
grade = pd.Series(['A','A','A'])

df = pd.DataFrame({'이름':nameSer,
                           '나이':age,
                           '성별':gender,
                           '학점':grade})

print(df)
