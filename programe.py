import random
top_of_range = input("Enter a number : ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    #print(type(top_of_range))

    if top_of_range <= 0 :
        print("Please type a number larger than 0 next time")
        quit()

else:
    print("Please enter a number next time ")
    quit()

random_number =  random.randint(0,top_of_range)
guess = 0

while True:
    guess+=1 
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Type a number next time")
        continue

    if user_guess == random_number:
        print("you got it ! ")
        break

    else:
        print("try again: ")

print("you got it in ", guess ," guesses")
