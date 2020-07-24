import cv2
import numpy as np

#read image
img=cv2.imread(r'E:\rose_flower.jpg')

#resize image
res=cv2.resize(img,(400,500))


kernel=np.array(([0,1,0],[0,1,1],[0,1,0]),np.uint8)

#different blur methods
blur=cv2.filter2D(res,-1,kernel)
avg=cv2.blur(res,(7,7))
gauss=cv2.GaussianBlur(res,(7,7),0)
median=cv2.medianBlur(res,5)
bilateral=cv2.bilateralFilter(res,5,100,100)
pot=cv2.GaussianBlur(res,(7,7),0)

#text on gauss image
font=cv2.FONT_HERSHEY_PLAIN
cv2.putText(pot,'Rose',(0,40),font,4,(255,0,0),3,cv2.LINE_4)

#flowerpot on image
cv2.line(pot, (50,250), (100,350), (0, 100, 0), 5)
cv2.line(pot, (200,270), (150,350), (0, 100, 0), 5)
cv2.line(pot, (100,350), (50,450), (0, 100, 0), 5)
cv2.line(pot, (150,350), (200,450), (0, 100, 0), 5)
cv2.line(pot, (50,450), (200,450), (0, 100, 0), 5)



#save all images
cv2.imwrite('2D filter.jpg',blur)
cv2.imwrite('Average filter.jpg',avg)
cv2.imwrite('Gaussian filter.jpg',gauss)
cv2.imwrite('Median filter.jpg',median)
cv2.imwrite('Bilateral.jpg',bilateral)
cv2.imwrite('text and pot.jpg',pot)


#showing output images
cv2.imshow('Resize',res)
cv2.imshow('Average blur',avg)
cv2.imshow('2D filter',blur)
cv2.imshow('Gauss',gauss)
cv2.imshow('Median',median)
cv2.imshow('Bilateral',bilateral)
cv2.imshow('Text and pot',pot)

cv2.waitKey(0)
cv2.destroyAllWindows()