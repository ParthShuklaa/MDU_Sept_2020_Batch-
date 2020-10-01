try:
    no  = int(input("Enter your Lucky No"))
    if no == 0:
        raise Exception("Exception throwth by If Block !!!")

    #print(no/Zero)


except ZeroDivisionError :
    print("You can't Divide  a no by Zero ....")

except NameError:
     print("Exception is raised, Handle it properly")

finally:
    print("Thank you for using our Application , Happily define variable!!!!")

open()
#exception throwth by If Block

f = open("demofile.txt", "r")
print(f.read())

