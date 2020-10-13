choice = "-"
available_parts= ["Monitor",
                  "Keyboard",
                  "Mouse",
                  "SSD",
                  "Optical Drive",
                  "Pendrive",
                  "Exit"  
                 ]
selected_choices=[]
available_choices=[str(i) for i in range(1,len(available_parts)+1)]
print(available_choices)

while choice!="0":
    if choice in available_choices:
        print("Adding {} ".format(choice))
        index=int(choice)-1
        selected_choices.append(available_parts[index])
    elif choice=='False':
        break

    else:
        print("Coose from the above list")
        for index, item in enumerate(available_parts):
            print("{}: {}".format(index+1,item))
    choice=input()
else:
    print("Have a nice day :)"  )
print(selected_choices)
            
