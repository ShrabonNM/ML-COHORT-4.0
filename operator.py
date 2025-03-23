a=20
b=10
x=a+b
y=a-b
z=a*b
w=a/b
print(x,y,z,w)

#floor division
f=9
g=2
h=f//2
#modulus 
j=f%g
print(h,j)


#if_else
p="Enter the value of X = "
q="Enter the value of Y = "
r= "Enter the value of Z = "
num1=input(p)
num2=input(q)
num3=input(r)

if num1>num2 and num1>num3:
    print("X is the largest Number")
elif num2>num1 and num2>num3: 
    print("Y is the largest Number")
else: 
    print("Z is the largest Number ")


 #if_else 
A = float(input("Enter the CGPA of Adnan = "))
B = float(input("Enter the CGPA of Rakib = "))
C = float(input("Enter the CGPA of Sakib = "))

if A > B and A > C:
    print("Adnan has the highest CGPA")
elif B > A and B > C:
    print("Rakib has the highest CGPA")
else:
    print("Sakib has the highest CGPA")

t = (A + B + C) / 3
print(f"The average CGPA is = {t:.2f}")



#bitwise not and or
 
u=4
w=7
s=u|w
i=u & w
print(u,w)





