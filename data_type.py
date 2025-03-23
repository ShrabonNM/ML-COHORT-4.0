a="Hello World"
print(a[1])#access element
print(len(a))

#check
txt="The best thing in life are free"
txt_1="The best thing in life are Free"
print("free" in txt_1)
print("free" in txt)

#slicing
a="Hello World"
print(a[2:5])

#upper and lower 
a="Hello World"
print(a.upper())
print(a.lower())

#string concatination/addition
a="Hello"
b="World"
c=a+" "+b
print(c)


#string formet using paceholder
a=20
text=(f"My name is Shrabon and I am {a} ")
print(text)





#1
a="ABRACADABRA"
print(a[2])
print(len(a))

#2
x="The quick brown fox jumps over the lazy dog"
print(x[10:19])

#3
A="বাংলা"
B="আমার"
C="সোনার"
txt=B+" "+C+" "+A
print(txt)

#4
Y="Ahnaf Tahmid Saad"
Z="ABRACADABRA"
text=(f"My favourite singer is {Y} .Whose most popular song is {Z}")
print(text)