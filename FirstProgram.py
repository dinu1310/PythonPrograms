i = 0
guessN = 60
while i < 5:
    gn = int(input("Guess The Number : "))
    if gn == guessN:
        print("congrats you have guessed correctly in ", +i+1, " attempt")
        break
    elif gn > guessN:
        print("sorry Guessed number is higher")
        print("attempt left ", +5-i-1)
        i = i+1
    else:
        print("sorry Guessed number is less")
        print("attempt left ", + 5 - i - 1)
        i = i + 1

    # *************************************************************************

me="dinu"
al=7
pr=f"this is a {me} {al}"
print(pr)

