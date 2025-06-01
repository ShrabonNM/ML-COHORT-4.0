

#Functions 


#functions are reusable blocks of code that perform a specific task. They can take inputs (arguments) and return outputs (results). Functions help organize code, make it more readable, and allow for code reuse.
#Defining a function
#function defination starts with the keyword 'def' followed by the function name and parentheses. Inside the parentheses, you can define parameters that the function can accept.
#Function without return value
def calculation(a, b): #parameters #a and b are the inputs to the function
    result = a + b
    print(result)
    


calculation(2,1) # 2, 1 are the arguments passed to the function. They are used as inputs for the parameters defined in the function.
calculation(3,6)
calculation(4,7)
calculation(10,15)

## Function with return value 
def calc_sum(c,d):
    result = c + d
    return result #return instead of print, the function will send the result back to the caller instead of displaying it immediately. This allows you to store, use, or print the result later.

total = calc_sum(1003,2344) # calling the function and storing the result in a variable
print(total) #This will print the result of the function call.



def print_hello():
    print("Hello Guys!")


print_hello() # calling the function to execute its code
print_hello() # calling the function again to see the output



#None function
def print_none():
    print("This function does not return anything.")
    # This function does not have a return statement, so it implicitly returns None.


output = print_none()  # Calling the function and storing the result in a variable
print(output) # This will print None, as the function does not return any value.


#🎯 Imagine This Situation:
#You go to a restaurant and order food.

#There are two things that can happen:

#The waiter tells you your food is ready (print) — you hear it, but you don’t get anything in your hand.

#The waiter brings your food to your table (return) — now you can eat it, take it home, or do something with it.

def just_print():
    print("Your food is ready.")

result = just_print()
print(result) #This function is useful just for displaying something.It’s simple and good when you don’t need the value later.






def give_food():
    return "🍔 Burger"

result = give_food()
print(result)
#In the first case, you just hear the message, but you can't do anything with it. In the second case, you get something tangible that you can use later.
#This is the difference between print and return in functions. Print shows a message, while return gives you something you can use later.
#The function returns something.You can store, print, change, or use it in calculations
#✅ Use case: Any time you want to reuse the result: in math, logic, web apps, AI, etc



#Why return is powerful
def square(x):
    print(x * x)

result = square(5)  # prints 25
print(result)       # prints None #You see the result, but can’t use it.
#In this case, the function prints the square of x but does not return it. The result is None because there is no return statement.

def square(x):
    return x * x

result = square(5)
print(result)       # 25
print(result + 10)  # 35 #You get the value and can use it again and again
#In this case, the function returns the square of x, allowing you to use the result in further calculations or operations.
#This is why return is powerful: it gives you a value that you can use later, while print just shows something on the screen.


def square(x):
    return x * x

result = square(5)
print(result)       # 25
print(result + 10)  # 35 You get the value and can use it again and again.
#In this example, the square function returns the square of x, which can be used in further calculations. The result is stored in the variable result, allowing you to use it multiple times.



def average(a,b,c):
    av=(a+b+c)/3
  #  print(av)


average(89,28,55)
print(average(89,28,55)) #This will print None because the function does not have a return statement.



def average_calc(a,b,c):
    ave=(a+b+c)/3
    print(ave)
    return ave  # This function now returns the average value.
# Calling the function and printing the result  
average_calc(88,77,41)
average_calc(56,88,234)



#There are two types of functions in Python: built-in functions and user-defined functions.
#Built-in functions are functions that are already defined in Python, such as print(), len(), and type(). 
# These functions are available for use without needing to define them yourself. it's called built-in because they are part of the Python language itself.
#User-defined functions are functions that you create yourself to perform specific tasks. 
# You define them using the def keyword, followed by the function name and parameters.


#Example of a built-in function
# The print() function is a built-in function that outputs text to the console.
print("Hello, World!")  # This will print "Hello, World!" to the console.
#Example of a user-defined function
print("Noor Mohammed","Shrabon")
print("Shahidul",end=" ") # This will print "Shahidul" without a newline at the end.
print("Mohammed",end=" ") # This will print "Mohammed" without a newline at the end.
print("Islam")


#In this example, we define a user-defined function called print_name that takes two parameters, first_name and last_name, and prints them together.
#now  #we can use the print function to print the first name and last name together.
print("Noor Mohammed","Shrabon",sep=" | ") # This will print "Noor Mohammed | Shrabon" with a separator of " | ".
#In this example, we define a user-defined function called print_name that takes two parameters, first_name and last_name, and prints them together.


print("United international",end="$$$") # This will print "United international" without a newline at the end and with "$$$" at the end.
print("University")# # This will print "University" on the same line as the previous print statement.
#In this example, we define a user-defined function called print_university that takes two parameters, university_name and location, and prints them together.



#Default parameters
##Default parameters allow you to define a function with default values for its parameters. If the caller does not provide a value for a parameter, the default value is used.
def calc_prod(a=2 ,b=1):
    print(a*b)
    
    
calc_prod()  # This will use the default values a=2 and b=1, so it will print 2.



def calc_prod1(a , b=3):
    sumation = a+b
    print(sumation)

calc_prod1(9)  # This will use the default value b=3, so it will print 12.




#TASK 

cities = ["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Sylhet"]
heroes = ["Iron" ,"Captain America", "Thor", "Hulk", "Black Widow"]
def print_len(list):
    print(len(list)) 

print_len(cities)  # This will print the length of the cities list, which is 5.
print_len(heroes)  # This will print the length of the heroes list, which is 5.


##Function to print each item in a list
def print_list(list):  # This function takes a list as an argument and prints each item in the list.
    for item in list:  # Iterate through each item in the list .we use a for loop to go through each item in the list.
        print(item , end=" ")


## Calling the function to print each item in the heroes and cities lists
print_list(heroes)  # This will print each hero in the heroes list.
print_list(cities)  # This will print each city in the cities list.

##Function to calculate the factorial of a number

def calc_fact(n):  # This function calculates the factorial of a number n and returns the result.
     fact = 1  # Initialize the factorial variable to 1.
     for i in range(1, n+1):  # Iterate from 1 to n (inclusive).
            fact *=1   # Multiply the current value of fact by i.
            print(fact) # Print the current value of fact at each step.
            return fact  # This function calculates the factorial of a number n and returns the result.
     
calc_fact(5)  # This will calculate the factorial of 5 and print the result.
calc_fact(10)  # This will calculate the factorial of 10 and print the result.
calc_fact(20)  # This will calculate the factorial of 20 and print the result.



#Function to convert USD to BDT
    
def converter(usd_amount): # This function converts a given amount in USD to BDT using a fixed exchange rate.
    bdt_amount = usd_amount * 122.13 # This is the exchange rate from USD to BDT.
    print(usd_amount, "USD =", bdt_amount, "BDT")  # Print the converted amount in BDT.
    print(bdt_amount,"BDT","=","USD",usd_amount)   ## Print the converted amount in USD.
 
converter(100)
converter(77)



# Home Task

def number_check(num):
    if num % 2 ==0:
        print(num,"this is an even number")
    else:
        print(num,"this is an odd number")
        
        
        
number_check(10)  # This will check if 10 is even or odd.
number_check(15)  # This will check if 15 is even or odd.
number_check(-3)




