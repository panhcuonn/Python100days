#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
seed_number=int(input("Enter seed number: "))
number=random.randint(0,1)
if number==0:
    print("Tails")
else:
    print("Head")