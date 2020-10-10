print("hello,and welcome user")
print("temperature")
def convert_temp():
    f=float(input("enter in fahrenheit"))
    c=5/9*(f-32)
    k=c+273.15
    return(k)
print(convert_temp())
def repeat():
    convert_temp()
print(convert_temp())
print('finished')