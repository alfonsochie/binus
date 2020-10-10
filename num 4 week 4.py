#u=new height
#z=desired width
def calc_height():
    w=int(input("enter current width"))
    h=int(input("enter current height"))
    z=int(input("desired width"))
    x,y=ratio(w,h)
    u=y*z/x
    print("the height:",u)
#
def ratio(width,height):
    while width % 2 == 0 and height % 2 == 0:
        ratio(width//2,height//2)
        break

    return(width,height)

calc_height()