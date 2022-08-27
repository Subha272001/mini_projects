#find compount interest

p=int(input("Principal : "))
t=int(input("Time :  "))
r=int(input("Rate : "))

ans = p*pow((1+r/100),t)
c_i_ = int(ans-p)
print(c_i_)
