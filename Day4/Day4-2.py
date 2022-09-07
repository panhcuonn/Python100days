import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#get the length of input
x=input("gieo que lay hen ")
random.seed(x)
x=len(names)
ran=random.randint(0,x-1)
print(names[ran]+" will play this bill")