import cv2
face_cascade = cv2.CascadeClassifier(r"/home/aiktc/Desktop/u/haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(r"/home/aiktc/Desktop/faceDetection.mp4")
#print(type(video))
check,frame=video.read()
while(check==True):
    check,frame=video.read()
    #frame_count+=1
    img=frame.copy()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(grey,
    scaleFactor=1.25,
    minNeighbors=14)
    for x,y ,w, h in face:
        frame=cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),3)
    cv2.imshow("face detector ",frame)

    print(type(face))
    print(face)

    cv2.imshow("first",frame)
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
cv2.destroyAllWIndows()



#print(video)
video.release()