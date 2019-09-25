import sys
from ImageRead import *
from ImageEncrypting import *
from ImageDecrypting import *

#Create objects for encrypting ,reading and decrypting
ImgRead=ImageRead()
ImgDecrypt=ImageDecrypting()
ImageEncrypt=ImageEncrypting()
#Get input and output paths
imgPath=sys.argv[1]
outputPath=sys.argv[3]
#Encrypt the message to array
img=ImgRead.readImageNpArray(imgPath)
ImageEncrypt.makeModuleFiveImage(img)
ImageEncrypt.encryptMessage(img,sys.argv[2])
#Decrypt message from the image
decImg=ImgRead.readImageNpArray(outputPath)
HiddenString=ImgDecrypt.decryptMessage(img)
print(HiddenString)
#Display the image
ImgRead.showImage(outputPath)

