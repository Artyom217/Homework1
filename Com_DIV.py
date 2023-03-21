a=24
b=36
d=16
def Gcd(x,y):
    z= int
    if x==0:
        return y
    elif y==0:
        return x
    else:
        z = x % y
        while z>0:
             x = y
             y = z
             z = x % y
        return y




print(Gd(Gd(a,b),d))