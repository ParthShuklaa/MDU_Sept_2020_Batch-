#WAP to Display your name five times along with Date and time
"""
Step1: Enter Your name and use For for diaplying it five times
For(inilization,Condition,Increment/decrement)
for (i = 0, i<10,<i++)
When i = 0 by default or i = i+1 , Do not write here in For loop

Step2: Include Datetime Module and then diaplay it

"""

import datetime
import time
Name = input("Enter your name \n")

for i in range(10):
    print(Name)
    CurrentDatetime = datetime.datetime.now()
    print(CurrentDatetime)
    time.sleep(1)
