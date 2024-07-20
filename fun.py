def userlogin():
    while True :
        user_name = input("Enter username ")
        password = input("Enter the password ")
        if user_name == "qiurong" and password == "qiurong0900":
            print("logining to the system")
            break
        else:
            print("Username or password is wrong try again")  
            continue  
        
userlogin()        
# def login():
#   while True:
#     username = input("What is your username?: ")
#     password = input("What is your password? ")
#     if username == "David" and password == "Replit4ev#r":
#       print("Welcome David!")
#       break
#     else:
#       print("That is not the correct username or password. Try again!")
#       continue
    
# print("REPLIT LOGIN SYSTEM")
# login()