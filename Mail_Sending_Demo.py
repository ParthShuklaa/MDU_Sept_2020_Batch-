"""
Step1: import Module smtplib
Step2: Creating connection
Step3: Sending Mail
Step4: Closing Connection

"""

import smtplib

from base64 import _bytes_from_decode_data

MyConnection = smtplib.SMTP('smtp.gmail.com', 587)
MyConnection.starttls()
MyConnection.login("username....","Password....")
MyMessage = "hi There, Tomorrow is Your Assessment. Come be prepared..!!"
MyConnection.sendmail("Sender Email"," Receiver Email ",MyMessage)
print("Mail Sent successfully, Check with receiver")
MyConnection.quit()

