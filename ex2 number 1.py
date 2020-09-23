h_feet=int(input("feet"))
h_inc=int(input("inches"))
h_inc=h_feet * 12
h_cm =round(h_inc* 2.54,1)
leght=(h_cm%88)

print("feet:",(h_feet))
print("inc:",(h_inc))
print((h_cm),"cm")
print("snowboard",(leght),"cm")
