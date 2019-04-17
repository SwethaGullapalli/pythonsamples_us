import json
with open("librarydata.json") as Libraryfile:
    Libraryfilecontents=Libraryfile.read()
    LibraryfileJson=json.loads(Libraryfilecontents)
    #print(LibraryfileJson)
    #print (LibraryfileJson["Library Details"]["Users"][0]["UserId"])
    UserIdentity=int(input("Enter ID card number: "))
    
def GetUserBooksDetails(Jsoninputdata,UId):
    match=0
    allotted=0
    for user in Jsoninputdata["Library Details"]["Users"]:
        #print (user["UserId"])
        if user["UserId"] == UId:
            match=1
            print("User name: ",user["UserName"])
            print("User Adress: ",user["Adress"])
            for userallotment in  Jsoninputdata["Library Details"]["Allotments"]:
                if userallotment["UserId"] == UId: 
                    #print(userallotment["ISBN"])
                    allotted=1
                    print("Number of books taken are: ",len(userallotment["ISBN"]))
                    print("Below are the details of the books taken by the user: ")
                    for book in Jsoninputdata["Library Details"]["Books"]:
                        if book["ISBN"] in userallotment["ISBN"]:
                            print ("Book Name: ",book["BookName"])
                            print ("Author: ",book["Author"]) 

            break
    if match == 0:
        print("User id is not valid")
    if allotted == 0:
        print("User did not take any books")
    
        
GetUserBooksDetails(LibraryfileJson,UserIdentity)