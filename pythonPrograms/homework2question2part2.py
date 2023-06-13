#Homework 2 Question 2 Second Method
#Jeremy Lampley

num=int(input("What number do you want to find the sqaure root of? "))

guess=float(input("Guess the square root. "))

threshold=1

while guess*guess != num:

    if num-guess*guess < 0:
        guess=(guess+num/guess)/2


    elif num-guess*guess < threshold:
              print(guess, " is close to the squareroot of ",num)
    

    elif num-guess*guess > threshold:
        print(guess, " is not the squareroot of ",num)

    else:
        break

    guess=(guess+num/guess)/2
    
print("Square root is ", guess)
