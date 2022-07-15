from bulkbikedata import columID, csvToDict, cleanDic ;


if __name__ == "__main__":
    identifiers = columID()
    cleanDic(csvToDict(identifiers),identifiers.title)
    