# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#split the location to x and y
location=position.split(',')
# determine the location
# column = x 
column=int(location[0])
# row = y 
row=int(location[1])

if column==1:
    row1[row-1]="x"
elif column==2:
    row2[row-1]="x"
elif column==3 :
    row3[row-1]="x"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")