#loops

count=1
while count<=10:
    print("Hello World", count)
    count+=1

i=1
while i<=100:
    print("Noor Shrabon",i)
    i+=1
# This loop will run idefinitely untill you stop it manually
i=1
while i<=10:
    print(i)
    i+=1


a=5
while a>0:
    print(a)
    a-=1

p=1
while p<=100:
    print(p)
    p+=1

q=100
while q>=1:
    print(q)
    q-=1



w=1
while w<=10:
    print(w*3)
    w+=1



nums=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(nums):
    print(nums[index])
    index+=1


heroes=["ironman","spiderman","hulk","thor","captain america"]
index=0
while index<len(heroes):
    print(heroes[index])
    index+=1

Places=["Dhaka","Chittagong","Sylhet","Rajshahi","Khulna"]#list
# This loop will print each place in the list
index=0 # Initialize index to 0
# This loop will run until index is less than the length of the Places list
while index<len(Places):
    print(Places[index])# Print the current place
    # Increment the index to move to the next place
    index+=1 # This will print "Dhaka", "Chittagong", "Sylhet", "Rajshahi", and "Khulna" in order
#tuple





jet_fighters=("F-16","F-15","F-18","F-22","F-35")#tuple
#tuple is immutable, so we cannot change the values in a tuple
index=0
while index<len(jet_fighters):
    print(jet_fighters[index])
    index+=1




numbers=(1,4,9,16,25,36,49,64,81,100)#tuple #tuple is immutable, so we cannot change the values in a tuple
# This loop will print each number in the tuple
i=0 # Initialize index to 0
x=36# The number we are looking for
# This loop will run until i is less than the length of the numbers tuple
while i<len(numbers): 
    if(numbers[i]==x):# If the current number is equal to x, we print the index
        print("Found at index",i)# Print the index where the number is found
    i+=1# Increment the index to move to the next number
# This will print the index of the number 36 in the tuple numbers
    


#break and continue
#break statement is used to exit the loop
#continue statement is used to skip the current iteration and continue with the next iteration
values=1
while values<10:
    print(values)
    if(values==5):
        break
    values+=1
else:
    print("Error")
    values+=1
print("Loop ended")


#break statement
# The break statement is used to exit the loop when a certain condition is met.

#break statement with if condition
# The break statement is used to exit the loop when a certain condition is met.

Animals=["cat","dog","elephant","tiger","lion"]#list
# This loop will print each animal in the list until it encounters "tiger", at which point it will break out of the loop.
index=0 # Initialize index to 0
while index<len(Animals): # This loop will run until index is less than the length of the Animals list
    # Print the current animal
    print(Animals[index]) 
    if(Animals[index]=="tiger"): # If the current animal is "tiger", we break out of the loop
        print("Found the tiger, breaking the loop") # Print a message indicating that we found the tiger
        break # Increment the index to move to the next animal
    # Increment the index to move to the next animal
    index+=1 # This will print "cat", "dog", "elephant", and then break when it reaches "tiger"
    

#continue statement
# The continue statement is used to skip the current iteration of the loop and continue with the next iteration.
p=0
while p<=5: # This loop will run until p is less than or equal to 5
    if(p==3): # This condition checks if p is equal to 3
        # If p is 3, we skip the rest of the loop and continue with the next iteration
        p+=1 # Skip the rest of the loop when p is 3
        continue # This will skip the iteration when p is 3
    print(p) 
    p+=1  # This will print 0, 1, 2, 4, 5 and skip 3
#continue statement with if condition



i=0
while i<=100:
   if(i%2==0):
     i+=1
     continue
   print(i) 
   i+=1


#Loops are used for sequential traversal of data structures like lists, tuples, and dictionaries.
#They allow you to perform operations on each element of the data structure without needing to manually access each element.
#For example, you can use a loop to iterate through a list of numbers and print each number.
   
        
list=[1,2,3,4,5,6,7,8,9,10]
for el in list:
    print(el) # el is the variable that takes the value of each element in the list during each iteration of the loop.
#The for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

vegetables=["carrot","potato","onion","tomato","cabbage"]
for val in vegetables:
    print(val) # This will print each vegetable in the list



name="akdjhenriirjs"#string
# Iterating through the string and printing each character
for char in name:
    print(char)




numbers=[1,4,9,16,25,36,49,64,81,100]#list
# Iterating through the list and printing each number
for element in numbers:
    print(element)


numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49, 64, 81, 100)#tuple #linear search
# This loop will search for the number 49 in the tuple numbers and print its index if found
x = 49
indx = 0

for element in numbers:
    if element == x:
        print("Found the number", indx)
    indx += 1  




seq = range (10) # The range function generates a sequence of numbers from 0 to 9
# You can use a for loop to iterate through this sequence
for i in seq:
    print(i)


seq = range(2,8)# The range function generates a sequence of numbers from 2 to 7
# You can use a for loop to iterate through this sequence
for i in seq:
    print(i)# This will print numbers from 2 to 7


seq = range(2, 20, 2) # The range function generates a sequence of even numbers from 2 to 18
# You can use a for loop to iterate through this sequence
for i in seq:
    print(i) # This will print even numbers from 2 to 18


seq = range(2, 10 ,3) # The range function generates a sequence of numbers starting from 2, ending before 10, with a step of 3
# You can use a for loop to iterate through this sequence
for i in seq:
    print(i) # This will print numbers 2, 5, and 8 because it starts at 2, ends before 10, and increments by 3 each time
# The range function generates a sequence of numbers starting from 0, ending before 10, with a step of 2


for i in range (3,15,2): # The range function generates a sequence of numbers starting from 3, ending before 15, with a step of 2
    print(i) # This will print numbers 3, 5, 7, 9, 11, and 13 because it starts at 3, ends before 15, and increments by 2 each time


for u in range(1,101):
    print(u)# This will print numbers from 1 to 100, one number per line


for u in range(100 ,0,-1):
    print(u)



multification=int(input("Enter he number:  ")) ## This will take an input from the user and store it in the variable multification
# The user will enter a number, and the program will print the multiplication table for that number
# The following loop will print the multiplication table of the number entered by the user
for i in range( 1,11):
    print(multification*i)# This will print the multiplication table of the number entered by the user from 1 to 10
# The following loop will print the multiplication table of the number entered by the user from 1 to 10



for i in range(1,10):
    pass
print("This is a placeholder loop that does nothing") # The pass statement is used as a placeholder when you don't want to write any code in the loop yet. It allows you to create an empty loop without causing an error.
# The pass statement is used as a placeholder when you don't want to write any code in the loop yet. It allows you to create an empty loop without causing an error.



#Task
count = 1
sum = 0
while count <= 10:
    sum += count
    count += 1
print("Total sum:", sum)



n=int(input("Enter a number: ")) # This will take an input from the user and store it in the variable n
sum=0
for i in range(1,n+1): 
        sum+=i # This will add the value of i to the sum variable
print("Sum is:", sum) # Print the result


n=int(input("Enter a number: ")) # This will take an input from the user and store it in the variable n
factorial=1
for i in range(1,n+1):
    factorial*=i # This will multiply the value of i with the factorial variable
print("Factorial of", n, "is", factorial) # Print the final result
# This will take an input from the user and store it in the variable n


