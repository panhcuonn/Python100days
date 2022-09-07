

import random


word=["red","green","blue"]
index =random.randint(0,len(word)-1)
letters=input("Guest a letter : ").lower()
choose_word= word[index]
numbers_loop=len(choose_word)
print(f"the word is {choose_word}")
# print("first solution")
# for i in range(0,len(choose_word)):
#     if choose_word[i] == letters:
#         print("right")
#     else :
#         print("wrong")
# print("second solution")
# for i in choose_word:
#     if i ==letters:
#         print("right")
#     else:
#         print("wrong")
i=0
# print("third solution")
while i<numbers_loop:
    if choose_word[i]==letters:
        print("right")
    else:
        print("wrong")
    i+=1