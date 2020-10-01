def reader():
    Data =  open("DemoFile.txt",'r')
    #print(Data.read())
    print(Data.readlines())

InputData = input("Enter your Message")
values = open("DemoFile.txt",'a+')
values.writelines(InputData)
values.close()

Data =  open("DemoFile.txt",'r')
print(Data.readlines())
Data.close()

reader()
