def ela(x):
    result=x%4
    if(result==0):
        print("Leap Year !")
    else:
        print("This is not leap year, Try Again !")

while True:
    print("Enter 1 to run !")
    print("Enter 2 to exit")
    x=int(input("Enter Your Choosen "))
    if(x==1):
        y=int(input("Enter your year "))
        ela(y)
    elif (x>=3):
        print("Enter Valid Choosen")
    else:
        print("Thank You !")
        break
