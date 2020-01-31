#placement

for stu in range(1,20+1):
    skill=input("Tell us ur skill")
    if skill=="java" or skill=="python" or skill=="script":
        if stu==1 or stu==3 or stu==5 or stu==2 or stu==6 or stu==10 or stu==14:
            print("Already booked")
        else:
            print("You are hired",stu)
