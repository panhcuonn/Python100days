# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#giai phap 1 la A%4 ==0->A/4 ==C -> C%100==0 thi chon
C= year /4
if C%100==0:
    print("Leap year.")
elif year/4==0:
    print("Leap year")
else:
    print("Not leap year.")

#400 = (2*2)*(2*2)*25
#4   = (2*2)
#100 = (2*2)*25
#chia het cho 4 nhung 
#ko chia het cho 100 tru truong hop 400
# goi A = A /4 ==0
# goi B thuoc B
# chon A*B neu B=4 
#giai phap 1 la A%4 ==0->A/4 ==100 thi chon
#
#