#python program for simple interest
def s_i_(p,t,r):
    return (p*t*r)/100

p=input("Principal : ")
t=input("Time :  ")
r=input("Rate : ")
print(s_i_(p,t,r))