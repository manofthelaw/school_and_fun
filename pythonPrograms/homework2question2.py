#Homework 2 Question 2
#Jeremy Lampley


x=int(input("Guess the square root of 27: "))

num=27.0
step=0.01

guess=x*x

if guess < num+step:
    while guess < num+step:

        x=(x+step)
        guess=x*x
        print(x)

else:
    while guess > num-step:
        x=(x-step)
        guess=x*x
        print(x)
        
print(guess)
