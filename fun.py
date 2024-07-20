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
