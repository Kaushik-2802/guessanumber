import random
num=random.randint(1,10)
print("welcome to the game all the best...\n")
print("enter 0 to exit the game...\n")
while True:
    guess=int(input("enter a number:"))
    if(guess==num):
        print("congratulations you have guessed the right number")
        break
    elif(guess>num):
        print("guessed too high try again")
    else:
      print("guessed too low try again")
    if(guess==0):
        break
print("the number generated was:",num)