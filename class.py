class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Student :
        def __init__(my_info,name,age):
            my_info.name = name
            my_info.age = age
            
            
            
        def myfunc(my_info):
                print("My name is : "+ my_info.name)
                print("And I am "+ str(my_info.age) + " years old")
                    
                
s1 = Student("Subha",21)
s1.myfunc()
    #print(s1.name)
    #print(s1.age)

        