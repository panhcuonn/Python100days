height = int(input("Enter your height : "))
age = int(input("Enter your age : "))
w_photo = input("Want a photo ?")
bill = 0
if height >120:
    if age <12 :
        bill +=5
    if age >=12 and age<18 :
        bill +=7
    if age > 18 and age <45:
        bill +=12
    elif age>45 and age <55:
        bill=0
    if w_photo == "Y":
        bill +=3
    print(f"Your bill is : {bill}")
else :
    print("You can not ride")