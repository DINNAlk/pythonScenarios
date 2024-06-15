def ela():
    A=open("ub.txt","w")
    F=open("u.txt")
    for i in F:
        A.write(i)
    F.close()
    A.close()
    print("Done !")

ela()
