import cv2
# all_images=glob.glob('*.jpg')
# print(all_images)
images =["galaxy.jpg","one.jpg"]
# print(type(img))
# print(img)
# print(img.shape)
for image in images:
    python_image=cv2.imread(image,0)
  
    resized_height=int(python_image.shape[0]/2)
    resized_width=int(python_image.shape[1]/2)
    resized_python_image=cv2.resize(python_image,(resized_width,resized_height))
    name="new"+image


    cv2.imwrite("new_img.jpg",resized_python_image)

print("done")
    # cv2.imshow("img.jpeg",resized_image)
    # cv2.waitKey(0)
    # c2v.destroyedAllWindows()