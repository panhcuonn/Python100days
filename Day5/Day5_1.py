# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
sum_heights=sum(student_heights)
number_students=len(student_heights)
average_heights=round(sum_heights/number_students)
print(average_heights)




#example 

# day_so=input("input chuoi so le ").split()
# for  x in range(0,5):
#     day_so[x]=int(day_so[x])
#     day_so[x]+=1
#     print(day_so[x])
    
    