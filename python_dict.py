


personal_info = {
       "name" : "subha",
        "age" : 21,
        "course" : "B.Tech",
        "blood_group" : "O+",
        "birth_year" : 2000,
        "birth_year" : 2001 #it will overwrite the birthyear from 2000 too 2001 
                            #changeable
     }
print(personal_info)
print(personal_info["name"])

#we can change or remove items
print(type(personal_info))  #<type 'dict'>
#Accessing items 
print(personal_info.get("name"))
print(personal_info.keys())  #accessing all keys
#Update the keys
personal_info['branch'] = "CSE"
print(personal_info)
print(personal_info.values()) #to get values of keys
print(personal_info.items())
#check existance
if "birth_year" in personal_info :
    print("Yes birth_year is present ")
personal_info.update({"name" : "Abhii"}) # if no updation does'nt show error 
print(personal_info) 
personal_info["name"] = "subha" 
print(personal_info)
personal_info.pop("blood_group")
print(personal_info)
personal_info.popitem()
print(personal_info)
del personal_info["age"]
print(personal_info)  # del can also delete the complete dictionary
#personal_info.clear()
#print(personal_info)
for x in personal_info:
 print(x)   #to print all key names
for x in personal_info:
 print(personal_info[x])  # to print all key values
for x in personal_info.values():
 print(x)
for x in personal_info.keys():
 print(x)
for x,y in personal_info.items():
    print(x,y)
#to copy dictionary
myinfo = personal_info.copy()
print(myinfo)
info = dict(myinfo)
print(info)

#Nested dictionary
myfriends = {
      'friend1':{
          "name" :"Jayanti",
          "nick_name" : "Victorious"
      },
      'friend2' :{
          "name" : "Priyanshi",
          "nick_name" : "Begum"
      },
      'friend3' :{
          "name" : "Abhii",
          "nick_name" : "Mendhak"
      }
  }
print(myfriends)

friend1={
          "name" :"Jayanti",
          "nick_name" : "Victorious"
      }
friend2 ={
          "name" : "Priyanshi",
          "nick_name" : "Begum"
      }
friend3 ={
          "name" : "Abhii",
          "nick_name" : "Mendhak"
      }
myfriends={
    'friend1': friend1,
    'friend2': friend2,
    'friend3': friend3
}
print(myfriends)
