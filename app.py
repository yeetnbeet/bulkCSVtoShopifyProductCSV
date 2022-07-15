from logging import PlaceHolder
from typing import Counter
from markupsafe import string
from numpy import size
import pandas as pd

#This is the columns you want from the csv
class columID :
    title = 'ProductText'
    sku = 'MaterialNumber'
    build = 'Spec'
    color = 'Color'
    taille = 'Size' 

identifiers = columID() 

# get only the columns you want from the csv file
df = pd.read_csv('DATA.CSV', usecols=[identifiers.title,identifiers.sku,identifiers.build,identifiers.color,identifiers.taille])
result = df.to_dict(orient='records')

dictByBike ={}
#Finds Variants From Duplicate Text and Parses them into an easy to read object (lists of variants)
def cleanDic(dict,identifier=string):
    dictByBike ={} 
    a = []   
    for item in dict :
        a.append(item[identifier])
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    for i in res :
        l = []
        for obj in dict:
            if i == obj[identifier]:
                l.append(obj)
        dictByBike[i]=l


    print("\n\n")    
    print(dictByBike)
    return dictByBike


if __name__ == "__main__":
    cleanDic(result,"ProductText")
    