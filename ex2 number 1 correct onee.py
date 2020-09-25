h_feet=int(input("feet"))
h_inc=int(input("inches"))
inc=h_feet * 12 + h_inc
h_cm =round(inc* 2.54,1)
percentage=88/100
leght=(h_cm*percentage)


print("feet:",(h_feet))
print("inc:",(inc))
print((h_cm),"cm")
print("snowboard",(leght),"cm")
