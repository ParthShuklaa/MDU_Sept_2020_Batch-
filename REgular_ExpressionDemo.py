import re

txt = "The rain in the Spain"
txt1= "The rain in the Spain during Christmas"


x = re.search("^The.*Spain$",txt)
x1 =re.search("^The.*Spain$",txt1)
print(x)
print(x1)
