"""
WAP to Convert Text to Speech
Step1: Import gtts Package/Lib with the help of pip Command
Step2: Creating object of gTTS class and saving output(.mp3)
Step3: Accessing Saved file (.mp3)

"""
import gtts
import os

MySpeech = gtts.gTTS(text="Hi Every one, I hope you are having fun learning python!!",lang = 'en',slow = False)
MySpeech.save("MySpeech1.mp3")
os.system("MySpeech1.mp3")
