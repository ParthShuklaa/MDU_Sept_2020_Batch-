"""
How to raise Exception
"""
try:
    raise FileNotFoundError ("Make sure Your Files are present in the System")
except FileNotFoundError :
    print("File Not Found Exception Occurs")
    raise   # To determine whether an exception was raised or not
