import random

def is_num(prompt):
    while True:
        choice = input(prompt)
        if choice.isnumeric():
            return int(choice)
        print("{} is not a number......".format(choice))
        print("Pleaase enter a valid no...")
highest = 1000
lowest= 1
answer = random.randint(lowest,highest)

print()

value = 1


while value!=0:
   
    value= is_num(": ")
    if   value == answer:
        print("{} you guessed it ".format(answer))

    elif value == 0:
        break
    elif value< answer:
        print("Enter higher no....")
    else:
        print("Enter Lower no...")
