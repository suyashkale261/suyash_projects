age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
nod = input("Enter your Number of Days : ")
if(age >= 18 and age < 30 and gender.upper() == "M"):
    amt = nod * 700
    print("Total Wages : ",amt)
elif(age >= 18 and age < 30 and gender.upper() == "F"):
    amt = nod * 750
    print("Total Wages : ",amt)
elif(age >= 30 and age <= 40 and gender.upper() == "M"):
    amt = nod * 800
    print("Total Wages : ",amt)
elif(age >= 30 and age <= 40 and gender.upper() == "F"):
    amt = nod * 850
    print("Total Wages : ",amt)
else:
    print("Enter Appropriate Age !!!!")
