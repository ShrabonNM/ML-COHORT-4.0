#list 
marks=[70.3,89.24,45.44,99.34,23.23,87.2]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])
print(marks[4])
multiple=["Ahnaf","Tahmid",79,92.2,"Saad"] # execute strings also
print(multiple)
print(type(multiple))
#strings are immutable it means in string , access is allowed but change of element is not allowed
#lists are mutable examples are above 
str="Hello"
print(str)
#str[0]="Y"  it's not possible / strings are immutable
#but in list the case is possuble examples are in below :
multiple[2]=("Shrabon")
print(multiple)


#list slicing
value=[32,35,23,45,28,34,32]
print(value[1:4])
print(value[:4]) # counted from 0
print(value[-3:-1])#counted from opposite site
value.append(47)# ***append adds one element at the end
print(value)

#sorting // used in ascending and descending 
values=[37,39,35,78,42]
values.sort()
print(values)
values1 = [37, 39, 35, 78, 42, 87]
values1.sort(reverse=True)
print(values1)
list1=['a','n','e','q','o']
print(list1.sort())
print(list1)
print(list1.sort(reverse=True))
print(list1)

#reverse // it's make the list completely opposite
list2=[3,4,5,2,1,8,9]
list2.reverse()
print(list2)

#insert
list3=[2,1,3]
list3.insert(1,5) # 5 inserted in the list
print(list3)

#remove
list4=[2,1,4,1]
list4.remove(1)
print(list4) #removed first 1 from list4

#pop
list5=[34,244,66,42,78,99]
list5.pop(3)
print(list5) # removed 3th element from the list