"""WAP FOR LISTS WITH EXAMPLES"""

"""Act = list(("number of doubts","number of books","number of questions","number of answers","number of buses","number of friends"))
kid={("walking giraffe","colors and shapes"):"fisher price",("the very hungry caterpillar","from head to toe"):"Eric carle","Interest":"Pretend play","Grade":1}
print (Act)
print (kid)"""

"""list and dict associated functions"""
"""
	list.append(obj)
Appends object obj to list

2	list.count(obj)
Returns count of how many times obj occurs in list

3	list.extend(seq)
Appends the contents of seq to list

4	list.index(obj)
Returns the lowest index in list that obj appears

5	list.insert(index, obj)
Inserts object obj into list at offset index

6	list.pop(obj=list[-1])
Removes and returns last object or obj from list

7	list.remove(obj)
Removes object obj from list

8	list.reverse()
Reverses objects of list in place

9	list.sort([func])
Sorts objects of list, use compare func if given


1	dict.clear()
Removes all elements of dictionary dict

2	dict.copy()
Returns a shallow copy of dictionary dict

3	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.

4	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary

5	dict.has_key(key)
Returns true if key in dictionary dict, false otherwise

6	dict.items()
Returns a list of dict's (key, value) tuple pairs

7	dict.keys()
Returns list of dictionary dict's keys

8	dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict

9	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict

10	dict.values()
Returns list of dictionary dict's values
"""
#associate data type with functions in daya to day activities

def microwave_oven(usermin,usersec):
    if(min==0):
        if(sec==60):
            min+=1
    elif(min>0):
        if(sec==60):
            min+=1
    elif(min==usermin):
        break
usermin=input("Enter  the minutes required")
usersec=input("enter the seconds required ")

microwave_oven(usermin)

#Visual studio editor components
"""Explorer,Search,Source Control,Debug,Extensions"""
#why list and dict data types have functions associated with them and others dont
"""because list and dict datatypes have set of values or data in it we can use functions on the set of data rather than on a single value like integers."""


