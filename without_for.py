shopping_list= ["bread","banana","eggs","milk","Potato"]
Shoppin_it=print("""Shopping items are as follows
Bread
Banana
Eggs
Milk
Potato""")
item_to_find=input("Enter a Shopping Item you would like to find:").lower()
print(item_to_find)
found_at = None
#for item in range(len(shopping_list)):
#	if shopping_list[item]==item_to_find:
#		found_at=item
#		break
if item_to_find in shopping_list:
    found_at=shopping_list.index(item_to_find)
if found_at is not None:
	print("{} is at {}".format(item_to_find,found_at))
else:
    print("{} is not in the Menu".format(item_to_find))
