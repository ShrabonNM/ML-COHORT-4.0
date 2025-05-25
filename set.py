# set is the collection of unordered item
#Each element of set must be unique and immutable but set is mutable
#here the difference is elements are immutable or not changeable and the set is changeable
#set does't store keys ,it only store values

collection={34,35,36,73,"shrabon"}
print(collection)
print(type(collection))
total={4,4,4,6,7,8,"shrabon","shrabon","noor"} 
print(total)#set ignores duplicate or repeated values
print(len(total))#length also ignored duplicate values

collection1={} # empty dictionary not set
print(collection1)
print(type(collection1))

#if we want to print empty set then we have to code in this way
collection11=set()
print(collection11) #printed empty set
print(type(collection11))# type of empty set



#several method of set
#add
collection11=set()
collection11.add(1)
collection11.add(2.3)
collection11.add(34)
collection11.add("shrabon")
print(collection11)
print(len(collection11))

#remove
collection11.remove(1)
print(collection11)
#We can remove anyting which is not existing in our set
#like we can not remove 7 because our set collecction11 does't containing 7

#clear
collection11.clear()
print(collection11) #clearing all element of set
print(len(collection11))


#pop
#it removes any random values from set
collection111={"coding","python","c++","java","c","R"}
collection111.pop()
print(collection111)
print(collection111.pop())


#union set 
#combain both sets values and returns new values

set1={4,5,6,7,1,3,9}
set2={1,2,3,4,5,6,7,8}
print(set1.union(set2)) #printing all elements of set1 and set2 variable
print(set1)# printing original values
print(set2)# printing original values


#intersection
#combain only common values of two sets
print(set1.intersection(set2)) #printing the common values of set1 and set2
print(set2.intersection(set1)) #printing the same values as like the previous line
print(set1) #printing the original set values
print(set2)#printing the original set values





#Task
task={"python","python","c","javascript","c++",
      "python",
      "java","java","c++"}
print(len(task)) #answer is 5 but we have given 9 elements in the set 
print(task)      #now question can come how the length become 5 the answer is 
                 #python never reads same elements and never prints same values in set.




#Task
# Task
values = {
   ("int", 9),
   ("float", 9.0)
}

print(values2344)
