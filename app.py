from logging import PlaceHolder
from typing import Counter
from numpy import product
import pandas as pd

# get only the columns you want from the csv file
df = pd.read_csv('DATA.CSV', usecols=['ProductText', 'MaterialNumber','Spec','Color','Size'])
result = df.to_dict(orient='records')

dictByBike ={}

def cleanDic(dict):
    dictByBike ={} 
    a = []   
    for item in dict :
        a.append(item["ProductText"])
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    for i in res :
        l = []
        for obj in dict:
            if i == obj['ProductText']:
                l.append(obj)
        dictByBike[i]=l


    print("\n\n")    
    print(dictByBike)

if __name__ == "__main__":
    cleanDic(result)