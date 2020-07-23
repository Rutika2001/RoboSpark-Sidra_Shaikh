import cv2

img=cv2.imread(r'E:/text.jpg',-1)             #read given image
cv2.imshow('image',img)
print(img)                                    #print all pixcels of image
h,w,c=img.shape
print(h,w)                                    #print height and width of image

img_resize=cv2.resize(img,(500,500))          #resize the image
cv2.imshow('Resize',img_resize)
print(img_resize)
h,w,c=img_resize.shape
print(h,w)                                    #print height and width of image

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     # conversion into grayscale image
cv2.imshow('Gray',gray)
cv2.imwrite('gray.jpg',gray)

Hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('Hsv',Hsv)
cv2.imwrite('Hsv.jpg',Hsv)

#threshholding
ret,thresh=cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
cv2.imshow('Binary thresh',thresh)
cv2.imwrite('Binary_thresh.jpg',thresh)

ret,thresh1=cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Bin_inversion',thresh1)
cv2.imwrite('Binary inv_thresh.jpg',thresh1)

#adaptive threshholding
thresh2=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,1)
cv2.imshow('Gaussian',thresh2)
cv2.imwrite('Gaussian adp_thresh.jpg',thresh2)

thresh3=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,1)
cv2.imshow('Mean_adp_thresh',thresh3)
cv2.imwrite('Mean_adp thresh.jpg',thresh3)


cv2.waitKey(0)
cv2.destroyAllWindows()