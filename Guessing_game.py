low= 1
high= 1000
print("Guess the Number you want Between {} to {} and I'll find it for YOU IN 10 Guesses".format(1,1000))
guess=1
guesses = 1
while True:
    guess = low +(high-low)//2
    High_low=input("I guess its {} , if it's not Press H for go Higher Or Press L to go Lower Or Press C if it is correct....".format(guess)).casefold()
    if High_low == "h":
        low = guess+1
    elif High_low == "l":
        high = guess+1
    elif High_low=="c":
        print("I guessed it in {} ".format(guesses))
        break
    else:
        print("Enter One of these H,L Or C")
        
    guesses+=1
