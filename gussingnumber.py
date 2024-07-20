correct_number = 1500 
attempt = 0 

while True:
    user_guess = int(input("pick number between 1 and 1000: " ))
    if user_guess <0:
        print("number is less then 0")
        exit()
    if user_guess < correct_number:
        print("the number is too low: ")
        attempt +=1
    elif user_guess > correct_number :
        print("the number is too high: ")
        attempt +=1 
    if user_guess == correct_number:
        print("you guess the correct number")
        break
    else:
        print("this is not the number i recognized", attempt) 



