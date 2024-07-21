# # def userlogin():
# #     while True :
# #         user_name = input("Enter username ")
# #         password = input("Enter the password ")
# #         if user_name == "qiurong" and password == "qiurong0900":
# #             print("logining to the system")
# #             break
# #         else:
# #             print("Username or password is wrong try again")  
# #             continue  
        
# # userlogin()        



# import random
# print("Infinity Dice 🎲")
  
# sides = int(input("How many sides?: "))
# playGame = "yes"
  
# def rollDice(sides):
#   print("You rolled ", random.randint(1,sides))
# while playGame == "yes":
#     rollDice(sides)
#     playGame = input("Roll again?")

# import os 
# import time
# for i in range(1,100):
#   print(i)
# os.system("clear")
# user_name = input("usernaem")  


def fizz_bizz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "buzz"
    return input    

print(fizz_bizz(15))     

