import json

with open ("library.json") as libraryFile:
    libraryFileContents = libraryFile.read()
    #print(libraryFileContents)
    libraryDataJson=json.loads(libraryFileContents)
    #print(libraryDataJson)
    #username="Swetha"
    username=input("Enter the username: ")
#print (libraryDataJson["Library Details"]["Allotments"][1]["UserName"])    

for  allotment in libraryDataJson["Library Details"]["Allotments"]:
    if allotment["UserName"]==username:
        for  books in allotment["Books"]:
            print(books)
    """if libraryDataJson["Library Details"]["Allotments"][i]["UserName"]==username:
        print (libraryDataJson["Library Details"]["Allotments"][i]["Books"])
    i=i+1
    if i>1:
        break  """  
