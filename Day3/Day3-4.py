# 🚨 Don't change the code below 👇
from tkinter import E


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
# #1st solution 
# if size =="S":
#     bill =15
#     if add_pepperoni=="Y":
#         bill+=2
#         if extra_cheese=="Y":
#             bill+=1
#             print(f"Your final Bill is : {bill}")
#         elif extra_cheese =="N":
#             print(f"Your final Bill is : {bill}")

#     elif add_pepperoni=="N":
#         bill =15
#         if extra_cheese=="Y":
#             bill+=1
#             print(f"Your final Bill is : {bill}")
#         elif extra_cheese =="N":
#             print(f"Your final Bill is : {bill}")

# elif size == "M":    
#     bill =20
#     if add_pepperoni=="Y":
#         bill+=3
#         if extra_cheese=="Y":
#             bill+=1
#             print(f"Your final Bill is : {bill}")
#         elif extra_cheese =="N":
#             print(f"Your final Bill is : {bill}")
#     elif add_pepperoni=="N":
#         bill=20
#         if extra_cheese=="Y":
#             bill+=1
#             print(f"Your final Bill is : {bill}")
#         elif extra_cheese =="N":
#             print(f"Your final Bill is : {bill}")


# elif size =="L":
#     bill =25
#     if add_pepperoni=="Y":
#         bill+=3
#         if extra_cheese=="Y":
#             bill+=1
#             print(f"Your final Bill is : {bill}")
#         elif extra_cheese =="N":
#             print(f"Your final Bill is : {bill}")
#     elif add_pepperoni=="N":
#         bill=25
#         if extra_cheese=="Y":
#             bill+=1
#             print(f"Your final Bill is : {bill}")
#         elif extra_cheese =="N":
#             print(f"Your final Bill is : {bill}")

#select size
if size == "S":
    bill+=15
elif size =="M":
    bill+=20
elif size =="L":
    bill +=25

#choose pepperoni 
if add_pepperoni =="Y":
    if size =="S":
        bill += 2
    else:
        bill += 3 
else:
    bill +=0

#extra pizza
if extra_cheese =="Y":
    bill+= 1
else:
    bill+= 0
    
print(f"You final bill is : {bill}")