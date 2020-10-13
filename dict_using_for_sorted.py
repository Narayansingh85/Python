#Using for loop only
dict1={
       1:'a',2:'b',3:'c',4:'d',
       }
for value in sorted(dict1.keys()):
    print("{} : {} ".format(value,dict1[value]))
