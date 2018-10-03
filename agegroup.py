def agegroup():
    age=int(input("Enter your age:"))
    if age>0 and age<=5:
        print ("you are toddler")
    elif age>5 and age<=12:
        print("you are minor")
    elif age>12 and age<=19:
        print ("you are teenager")
    elif age>19 and age<35:
        print ("you are in young age")
    elif age>35 and age<60:
        print ("you are in middle age")
    elif age>65 and age<150:
        print ("you are in old age")
        cal(agegroup())
    else:
        print ("You are Alien")
        cal(agegroup())

agegroup()
