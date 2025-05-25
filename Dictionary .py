#Dictionary 
#Dictionaries are used to store data values in key-value pair
#They are unordered ,mutable(changeable) & don't allow duplicate keys


info ={
    "Name": "Shrabon",
     "ID":2487308,
     "Istitution":"UIU",
     "Avg_Marks":94.5,
     "GPA":4.00,
     "Course":"CC392",
     "Section":"LB",
     "Course":("OOP","JAVA","Python","ML","C"),
     4545:"99%",
     1232:345,
     "Promoted_to_next_course":True,
}
print(info)
print(type(info))

# Accessing the 'Course' key
print(info["Course"]) #accessing the index

# Updating the 'Name' key
info["Name"] = "Noor"   #assigning new value and removing the previous one
print(info)  
               


#null dic
null_dic={

}
null_dic["name"] = "Mohammed"
print(null_dic)




#nested dictionary

students={

       "name":"Shrabon",
       "subjects":{
           "phy":87,
           "chem":79,
           "bio":88,
           "nath":83
       }

}

print(students)
print(students["subjects"]) #accessing 
print(students["subjects"]["chem"]) #accessing to the nested dictionary

#key;s printing 
print(info.keys()) # printing all keys of info dictionary
print(list(info.keys())) # type casting to list 

# length of dictionary
print(len(info.keys()))
print(len(list(info.keys())))

#value 
print(info.values()) #vgetting the values of all keys 

#items
print(info.items())  #returns all (keys and values) pairs as tuples
print(list(info.items()))
paris=list(info.items())
print(paris[0]) #accessing the indivisual tuples


#get 
#returns the key accoring to the value

print(info.get("Name"))
print(info.get("name233")) #though name233 has no exist in the dictonary but it wii not give any error
                           #it will show 'NONE' .That is the main speciality of get.()'
#if we want to print name233 without get.() then our output will show error



#update 

info.update({"city" : "Cumilla"}) #update a new key to the main dictonary
print(info)
print(info.update({"city" : "Cumilla","age" :"xxxxx"}))




#Task 1


task={
     "table":["a piece of furniture","list of facts and figures"],#we can set the element of keys in both ways in list and tuple,(),[]
      "cat": "a small animal"
}
print(task)
print(type(task))



#Task

marks1 = {}

x = int(input("Enter the physics marks: "))
marks1.update({"physics": x})

x = int(input("Enter the math marks: "))
marks1.update({"math": x})

x = int(input("Enter the chemistry marks: "))
marks1.update({"chemistry": x})

print(marks1)
