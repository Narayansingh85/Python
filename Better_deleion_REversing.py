list1=[300,600,200,500,100,4,3,5,6,23,45,34,22,56,78]
min1 = 23
max1 =200
for index in range(len(list1)-1,-1,-1):
    if list1[index] < min1 or list1[index] > max1:
        del list1[index]
print(list1)
