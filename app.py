from bulkbikedata import columID, csvToDict, cleanDic ;
import csv ;

def bikeDataToList(bikedata):
    bikedatalist = ['Handle','Title','Body(HTML)','Vendor','Standardized Product Type',
    'Custom Product Type','Tags','Published','Option1 Name','Option2 Name',
    'Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Grams',
    'Variant Inventory Tracker','Variant Inventory Policy','Variant Fulfillment Service','Variant Price','Variant Compare At Price',
    'Variant Requires Shipping','Variant Requires Shipping','Image Src','Image Position','Image Position',
    'Gift Card','SEO Title','SEO Description','Google Shopping / Google Product Category','Google Shopping / Gender',
    'Google Shopping / Age Group','Google Shopping / MPN','Google Shopping / AdWords Grouping','Google Shopping / AdWords Labels','Google Shopping / Condition',
    'Google Shopping / Custom Product','Google Shopping / Custom Label 0','Google Shopping / Custom Label 1','Google Shopping / Custom Label 2','Google Shopping / Custom Label 3'
    ,'Google Shopping / Custom Label 4','Variant Image','Variant Weight Unit',
    'Variant Tax Code','Status'
    ]
    return bikedatalist

def writeShopifyCSV (bikedata,path) :
    with open(path, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        
        # write a row to the csv file
        writer.writerow(bikedata)


if __name__ == "__main__":
    identifiers = columID()
    bikeData = cleanDic(csvToDict(identifiers),identifiers.title)
    print("\n\n\n\n\n",bikeData)
    writeShopifyCSV(bikeDataToList(bikeData),'OUTPUT.CSV')
    