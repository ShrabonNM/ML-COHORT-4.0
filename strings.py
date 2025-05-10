#string
#concating
str1="Hello everyone, I am Noor Mohammed Shrabon.\n"
str2="I am 20 years old"
print(str1+str2)



#length
str3="United"
len3=len(str3)
print(len3)
str4="International"
len4=len(str4)
print(len4)
str5="University"
len5=len(str5)
print(len5)
final_str=str3+" "+str4+" "+str5
print(len(final_str))



#indexing 
str6="Private Universites"
print(str6[4])
print(str6[0])
print(str6[7]) #space ashbe


#slicing 
str7="Public Universities"
print(str7[1:5])
print(str7[7:11])
print(str7[10:17])
print(str7[-4:-1])  #negative index


#string functions
str="i am a coder.I love to code."
str.endswith("er.")
print(str.endswith("er."))
#capitalized
str=str.capitalize()
print(str)
#replacing 
print(str.replace("co","lea"))
#finding
print(str.find("d"))
#count
print(str.count("code"))


#practics
user_name=input("Enter your username: ")
print("The length of your username is : ",len(user_name))

symbol="Hi, I am a $ symbol . Do you need $?.I can give you $"
print(symbol.count("$"))