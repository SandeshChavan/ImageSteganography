from ImageRead import *
from ImageEncrypting import *
from ImageDecrypting import *

ImgRead=ImageRead()
ImgDecrypt=ImageDecrypting()
ImageEncrypt=ImageEncrypting()
imgPath="D:\\Sandy\\ImageProcessing\\ImageDataSet\\standard_test_images\\standard_test_images\\lena_gray_512.tif"
outputPath="C:\\Users\\pc\\PycharmProjects\\ImageSteganographyOOPs\\Test.png"
img=ImgRead.readImageNpArray(imgPath)
ImageEncrypt.makeModuleFiveImage(img)
ImageEncrypt.encryptMessage(img,"Testing Image Steganography")
decImg=ImgRead.readImageNpArray(outputPath)
HiddenString=ImgDecrypt.decryptMessage(img)
print(HiddenString)
ImgRead.showImage(outputPath)

