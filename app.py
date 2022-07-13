import pandas as pd

# get only the columns you want from the csv file
df = pd.read_csv('DATA.CSV', usecols=['ProductText', 'MaterialNumber','Spec','Color','Size'])
result = df.to_dict(orient='records')

dictByBike ={}

def cleanDic(dict):
    dictByBike ={}
    variant = {}
    aggregator = {}
    counterV = 0
    counterT = 0
    counterD = 0
    currentProduct = dict[0]["ProductText"]
    lastProduct = ""
    lenOfdict = len(dict)
    for object in dict :
        print(lastProduct)
        if object ["ProductText"] == currentProduct and counterT <= lenOfdict-2 :
            aggregator[counterV] = {"SKU":object['MaterialNumber'],
            'SPEC':object['Spec'],
            'Color':object['Color'],
            'Size':object['Size']
            }
            variant[currentProduct] = aggregator[counterV]
            counterT = counterT+1
            counterV = counterV+1
            lastProduct = currentProduct
            currentProduct = dict[counterT]["ProductText"]
        else :
            counterD = counterD + 1
            dictByBike = variant
            counterT = counterT+1
            counterV = 0
            lastProduct = currentProduct
            if counterT <= lenOfdict -2 : 
                currentProduct = dict[counterT]["ProductText"]
                variant = {}





    print(dictByBike) 

if __name__ == "__main__":
    cleanDic(result)