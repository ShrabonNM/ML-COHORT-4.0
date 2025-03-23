# for loop
# while loop

# infinity 

#curly braces {}  
# parenthesis
# array - containers 
fruits=["apple ","banana","cherry"]  #list
for x in fruits:
   print(x)


for x in range(10) :
   print(x)


number = 1
# Outer loop for rows
for i in range(3):
    # Inner loop for columns
    for j in range(3):
        print(number, end=" ")  # Print the number with a space
        number += 1  # Increment the number
    print()  # Move to the next line after each row



 #while loop 
i = 0
number = 1

while i in range(3):  # Outer loop for 'i'
    j = 0
    while j in range(3):  # Inner loop for 'j'
        print(number, end=" ")
        number += 1
        j += 1
    print()  # To move to the next line after inner loop finishes
    i += 1



