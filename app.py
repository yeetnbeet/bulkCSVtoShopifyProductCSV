import json
from typing import Counter
from bulkbikedata import columID, csvToDict, cleanDic ;
import csv ;
import json ;

def bikeDataToList(bikedata,vendor='BMC'):
    bikedatalist = ['Handle','Title','Body(HTML)','Vendor','Standardized Product Type',
    'Custom Product Type','Tags','Published','Option1 Name','Option1 Value','Option2 Name',
    'Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Grams',
    'Variant Inventory Tracker','Variant Inventory Policy','Variant Fulfillment Service','Variant Price','Variant Compare At Price',
    'Variant Requires Shipping','Variant Taxable','Variant Barcode','Image Src','Image Position','Image Position',
    'Gift Card','SEO Title','SEO Description','Google Shopping / Google Product Category','Google Shopping / Gender',
    'Google Shopping / Age Group','Google Shopping / MPN','Google Shopping / AdWords Grouping','Google Shopping / AdWords Labels','Google Shopping / Condition',
    'Google Shopping / Custom Product','Google Shopping / Custom Label 0','Google Shopping / Custom Label 1','Google Shopping / Custom Label 2','Google Shopping / Custom Label 3'
    ,'Google Shopping / Custom Label 4','Variant Image','Variant Weight Unit',
    'Variant Tax Code','cost','Status'
    ]
    bikedatalistPrintable = ['','','','','',
    '','testing:sammachine','','','Option1 Value','',
    '','','','Variant SKU',0,
    'shopify','deny','manual','','',
    'TRUE','TRUE','','','',
    'FALSE','','','','',
    '','','','','',
    '','','','',''
    ,'','','lb',
    '','',''
    ]
    shopifyReadylist = []
    shopifyReadylist.append(bikedatalist)
    bikename = ''
    Counter = 0
    with open('OUTPUT.CSV', 'w') as f:
    # create the csv writer
        writer = csv.writer(f)
        writer.writerow(bikedatalist)
        for key in bikedata:
            for i in bikedata[key]:
                Counter = Counter + 1
            
                if i["ProductText"] != bikename:
                    printablecopy = bikedatalistPrintable
                    printablecopy[1] = i["ProductText"]
                    printablecopy[3] = vendor
                    printablecopy[5] = "Bikes"
                    printablecopy[7] = "TRUE"
                    printablecopy[8] = "Size"
                    printablecopy[9] = i["Size"]
                    printablecopy[14] = i['MaterialNumber']
                    printablecopy[46] = "Draft"
                    shopifyReadylist.append(printablecopy)
                    print("HEAD",",",bikename,Counter)
                    print(printablecopy)
                    writer.writerow(printablecopy)
                    printablecopy = []
                    bikename = i["ProductText"]
                elif i["ProductText"] == bikename:
                    printablecopy = bikedatalistPrintable
                    printablecopy[1] = ""
                    printablecopy[3] = ""
                    printablecopy[5] = ""
                    printablecopy[7] = ""
                    printablecopy[8] = ""
                    printablecopy[9] = i["Size"]
                    printablecopy[14] = i['MaterialNumber']
                    printablecopy[46] = ""
                    printablecopy[9] = i["Size"]
                    printablecopy[14] = i['MaterialNumber']
                    shopifyReadylist.append(printablecopy)
                    print("SUB",",",bikename,Counter)
                    print(printablecopy)
                    writer.writerow(printablecopy)
                    printablecopy = []

    

                    
        
    return shopifyReadylist





if __name__ == "__main__":
    identifiers = columID()
    bikeData = cleanDic(csvToDict(identifiers),identifiers.title)    
    ttt = bikeDataToList(bikeData,'bmc')
   
    for line in ttt:
        print(line)
    
    
    