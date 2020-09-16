#WAP to INPUT user name and Age
Name  = input("Enter your Name ?\n")
Age   = int (input("Enter your Age in Years ?\n"))


DatatypeofAge = type(Age)
DatatypeofName = type(Name)
print(DatatypeofAge)
print(DatatypeofName)
#Displaying name using + Concatenation
print("Your name is "+Name)
#print("Your Age is "+Age)

#Check if User is eligible for Voting
if Age >= 18:
    print("you can vote")
else:
    print("You can't vote, Watch POGO.!!!!")



print("Thank you for using my Application ")