import cv2

face_cascade = cv2.CascadeClassifier(r"/home/aiktc/Desktop/u/haarcascade_eye.xml")
img=cv2.imread(r"",1)

grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(grey_img,
scaleFactor=2.4,
minNeighbors=5)
print(type(face))
print(face)

for x,y ,w, h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),3)

cv2.imshow("face detector image",img)
cv2.waitKey(0)
cv2.destroyAllWindow()
