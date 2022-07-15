import json
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
    for key in bikedata:
        for i in bikedata[key]:
            printablecopy = bikedatalistPrintable
            if i["ProductText"] != bikename:
                printablecopy[1] = i["ProductText"]
                printablecopy[3] = vendor
                printablecopy[5] = "Bikes"
                printablecopy[7] = "TRUE"
                printablecopy[8] = "Size"
                printablecopy[9] = i["Size"]
                printablecopy[14] = i['MaterialNumber']
                printablecopy[46] = "Draft"
                shopifyReadylist.append(printablecopy)
                
                bikename = i["ProductText"]
            else:
                printablecopy[9] = i["Size"]
                printablecopy[14] = i['MaterialNumber']

                    
        
    return shopifyReadylist





if __name__ == "__main__":
    identifiers = columID()
    bikeData = cleanDic(csvToDict(identifiers),identifiers.title)    
    ttt = bikeDataToList(bikeData,'bmc')
    print("\n\n\n\n\n\n",ttt)
    
    