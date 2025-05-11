lights=input("Enter the colour: \n")

if(lights=="Red"):
    print("Stop\n")
elif(lights=="Green"):
    print("Go\n")
elif(lights=="Yellow"):
    print("Wait\n")
else: 
    print("Not a valid colour\n")
    

n=6
if(n==2):
    print("Greater than 2\n")#indentaiton (if er por print er age er space ke bole)
elif(n<9):
    print("Less than 9\n")



Grade = int(input("Enter the obtained marks: "))

if Grade >= 90 and Grade <= 100:
    print("A Grade\nCongratulations")
elif Grade >= 80 and Grade <= 89:
    print("Grade B\nGood Marks")
elif Grade >= 70 and Grade <= 79:
    print("Grade C\nNot Bad")
elif Grade >= 60 and Grade <= 69:
    print("Grade D\nWork Hard")
elif Grade >= 0 and Grade <= 59:
    print("F Grade\nTry Again")
else:
    print("Invalid Number")



number=int(input("Enter the Number:  \n"))
if(number%2==0):
    print("Even")
else:
    print("Odd")



a=int(input("Enter the value of a=  "))
b=int(input("Enter the value of b=  "))
c=int(input("Enter the value of c=  "))
if(a>b and a>c):
    print("A is the greatest value" )
elif(b>a and b>c):
    print("B is the greatest value")
elif(c>a and c>b):
    print("C is the greates value")




value=int(input("Write the number :  \n"))
if(value%7==0):
    print("It's multiple of 7\n")
else:
    print("It's not multiple of 7\n")