import cv2

img=cv2.imread('./img/images.jpg', 1)

print(img.shape)

h, w, c =img.shape
print("Hight,Width,pixel:-")

print(type(img))
print(img.dtype)
print(img)
