#tuple
#tuple is also immutable
list=(293,284,294,510,304)#generally used by parentheses 
print(list)
print(type(list))
print(list[0])#access is possible in tuple
print(list[3])
#list[2]=847 #assigning is not allowed
#print(list)


#if we use single values in tuple then we need to use ','/coma after the value .
#the value can be string ,float or integer
tup1=("hello",)
print(type(tup1))
tup2=(3.3,)
print(type(tup2))
tup3=(3,4,6,8,1,2,)
print(tup3[1:3])
print(tup3.index(2)) #counted where the element is located
print(tup3.count(6)) #how many 6 is exixting in this tuple will be counted


#task
movies=[]
mov1=input("Enter the movies name1: ")
mov2=input("Enter the movies name2: ")
mov3=input("Enter the movies name3: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#task2
#palindrom means elements will be same if we read it from both side right and left
list=[2,3,4,3,2]
list_copy=list.copy()
list_copy.reverse()
if (list_copy==list):
    print("Palindrom\n")
else :
    print("Not Palindrom\n")



#task
grade=('A','A','C','F','D','B','A')
print(grade.count('A'))
grade1=['A','A','C','F','D','B','A']
grade1.sort()
print(grade1)