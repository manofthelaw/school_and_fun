height=int(input("What is the height (in meters) of the tower? "))

while height < 0:
    print("Give me another height, positive please.")
    height=int(input("What is the height (in meters) of the tower? "))

time=int(input("How long has the ball been falling? (in seconds) "))


while time < 0:
    print("Give me another time, positive please.")
    time=int(input("How long has the ball been falling? (in seconds) "))


while 1:
    accel=9.8
    distance= 1/2 * accel * time * time
    new_height= height - distance

    if new_height > 0:
        print("The ball is ", new_height, "meters from the ground.")
        

    elif new_height < 0:
        print("The ball hit the ground before this time")
        break

    time =int(input("Check another time "))
