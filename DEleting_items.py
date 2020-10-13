list1=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
min_val=3
max_val=9
stp=0
for index,value in enumerate(list1):
    if value>=min_val:
        stop=index
        break
del list1[:stop]
for index in range(len(list1)-1,-1,-1):
    if list1[index]<= max_val:
        stop=index+1
        break
del list1[stop:]
print(list1)
