#hours=float(input("enter hours"))
#minutes=float(input("enter minutes"))
#seconds=float(input("enter seconds"))
#s=seconds/60
#m=(minutes+s)/60
#h=(hours+m)/24
#print (h,'days')


print("convert_to_days")
def convert_to_days():
    t1 = float(input("enter hours"))
    t2 = float(input("enter minutes"))
    t3 = float(input("enter seconds"))
    minutes = t3 / 60
    hours = (minutes+t2) / 60
    day = (hours+t1) / 24
    return (day)

print(convert_to_days())