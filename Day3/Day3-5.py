# 🚨 Don't change the code below 👇
from turtle import st


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#1,combine name 
both_name =name1 + name2 
#2,cast lowercase
both_name_lower=both_name.lower()
#3,count words
t_word=both_name_lower.count('t')
r_word=both_name_lower.count('r')
u_word=both_name_lower.count('u')
e1_word=both_name_lower.count('e')
count_true= t_word+r_word+u_word+e1_word

l_word=both_name_lower.count('l')
o_word=both_name_lower.count('o')
v_word=both_name_lower.count('v')
e2_word=both_name_lower.count('e')
count_love=l_word+o_word+v_word+e2_word

#4,result 
result =str(count_true)+str(count_love)
if int(result)<10 or int(result)>90:
    print(f"Your score is {result}, you go together like coke and mentos")
elif int(result)>40 and int(result)<50:
    print(f"Your score is {result}, you are alright together")
else :
    print(f"Your score is {result}")    
