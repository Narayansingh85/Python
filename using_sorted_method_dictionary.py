#Always sort dictionary before using it because it will change randomly
dictionary1={'1':'Papa','2':'Mama','3':'Big brother','4':'Younger brother','5':'Me',}
#keys_list=list(dictionary1.keys())
#keys_list.sort()
#print(keys_list)
keys_list=sorted(list(dictionary1.keys()))
for values in keys_list:
    print(dictionary1[values],end="\n")
'''
for i in range(10):
    for value in dictionary1:
        print(value,dictionary1[value])
    print('-'*80)
'''
