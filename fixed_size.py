import cv2
import os

width = 512
height = 512
dimension = (width,height)

ext = [".jpg",".png",".jpeg",".JPG"]

def loadImages(path = "."):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(tuple(ext))]


filenames = loadImages()
images = []
resize_image = []

for file in filenames:
    images.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))

for image in images:
    re = cv2.resize(image,dimension,interpolation=cv2.INTER_AREA)
    resize_image.append(re)

num = 1
for i in resize_image:
    cv2.imwrite("database/"+str(num)+".jpg",i)
    print("saving", num)
    num += 1
