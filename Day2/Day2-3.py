# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#casting age as int
age_as_int =int(age)
#calculate the days,weeks and months in 90 years
days_in_90years=90*365
week_in_90years=90*13*4
month_in_90years=90*12
#calculate the days,weeks and months in 90 years
days_left=days_in_90years - (age_as_int*365)
week_left=week_in_90years - (age_as_int*52)
month_left=month_in_90years - (age_as_int*12)

print(f"you have {days_left} days, {week_left} weeks and {month_left} months left.")

