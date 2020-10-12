def fizz_buzz(no: int)->str:
    """Play fizz_buzz
    :param: The no to check
    :return: 'fizz' if no is divisible by 3
                'buzz' if no is divisible by 5
              'fiz buzz' if no is divisible by 3 and 5
    """
    if no%3==0 and no%5==0 :
        return "fizz buzz"
    elif no%3==0:
        return "fizz"
    elif no%5==0:
        return "buzz"
    else:
        return str(no)
input("Press Enter to start...")
print()
next_number = 0
while next_number <99:
    next_number+=1
    print(fizz_buzz(next_number))
    next_number+=1
    correct_answer=fizz_buzz(next_number)
    users_choice=int(input("Your Turn >>"))
    users_answer=fizz_buzz(users_choice)
    if users_answer != correct_answer:
        print("You LOSE try again Next time...")
        break
else:
    print("Well done you made it {}".format(next_number))
