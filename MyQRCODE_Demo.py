import pyqrcode
Email = "parth.shukla@9ledgepro.com"
Linkedin ="https://www.linkedin.com/in/parth-shukla-09205239/"
GithubProfile = "https://github.com/ParthShuklaa"
MobileNo = "9599587014"

MyQRCODE = pyqrcode.create(Email+" \n"+Linkedin+" \n"+GithubProfile +"\n"+ MobileNo)
MyQRCODE.svg("MyDetails.svg")
print("Congrautlations, Your QRcode is created!!! Hurray....")