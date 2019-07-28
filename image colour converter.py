import cv2

img=cv2.imread("visual.jpg ",0) #-1 for colour image 0-for black and white 
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("visual",resized_image)
cv2.imwrite("image.jpg",resized_image)#for making new image or resized image
cv2.waitKey(0) # 0 for long time
cv2.destroyAllWindows()
