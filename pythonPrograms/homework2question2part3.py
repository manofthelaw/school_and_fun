#Homework 2 Question 2 Method 3
#Jeremy Lampley

num=int(input("Give me a number to square root! "))

threshold=0.05

xStart=0
xEnd=num
xMiddle=xEnd/2

while xMiddle**2 != num:

    if xMiddle**2 > num+threshold:
        xEnd=xMiddle
        xMiddle=xMiddle/2

    elif xMiddle**2 < num-threshold:
        xStart=xMiddle
        xMiddle=(xEnd+xStart)/2

    else:
        break

print(xMiddle)
