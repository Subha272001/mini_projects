#find factorial number
def factorial(num):
      if num==0 or num==1:
         return 1
      else:
         return num* factorial(num-1)  


num=input("Number : ")
print(factorial(num))