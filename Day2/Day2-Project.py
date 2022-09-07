from typing import final


print("Welcome to the tip calculator.")
total_bill=input("What was the total bill ? ")
tip_per=input("What was the percentage tip would you like to give? 10,12 or 15?")
people_split=input("How many people to split the bill? ")

#casting variables
total_bill_as_float=float(total_bill)
tip_per_as_int=int(tip_per)
people_split_as_int=int(people_split)

#calculate the bill have tip
bill_after_have_tip=total_bill_as_float*(tip_per_as_int/100+1)

#calculate money each people should pay
money_each_people_should_pay=bill_after_have_tip/people_split_as_int

#rounding the bill
final_bill=round(money_each_people_should_pay,2)

#print the final bill
print(f"Each person should pay: {final_bill}")