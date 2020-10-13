#Sictionaries are here
bike = {"make1": "Honda","model_H": "Dazzler","colour_H": "black","engine_size_H": 160,
        "make2": "Suzuki","model_s": "Busa","colour_S": "red","engine_size_S": 1500,
        "make3": "Tvs","model_T": "Shine","colour_T": "White","engine_size_T": 125,
        "make4": "Royal_Grey","model_E": "Bullet","colour_E": "red","engine_size_E": 300,
        "make5": "Bajaj","model_B": "Discover","colour_B": "Blue","engine_size_B": 100,
        }
#print(bike["engine_size"])
#print(bike["colour"])
def options(dict1):
    for key,item in dict1.items():
        print("{}:{}".format(key,item))
options(bike)
print()
while True:
    print()
    print("Choose form the options avaialable Above")
    print()
    print("Enter quit to move out of the menu")
    print()
    choice=input("Enter the information you wanna know.").casefold()
    if choice=='quit':
        break
    print()
    show = bike.get(choice,choice+" is not available")
    print(show,end='\n')
    '''elif choice in bike:
        show=bike.get(choice)
        print(show)
    '''
    if show not in bike:
        print()
        print("Enter from the given options  :)",end="\n")
        options(bike)
    
