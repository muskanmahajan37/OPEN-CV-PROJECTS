import numpy as np
import cv2


img = cv2.imread(r"D:\Coordinate-Detection\test_image.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



lower_blue = np.array([110,50,50]) 
upper_blue = np.array([130,255,255])
blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)

lower_yellow = np.array([26,50,50])
upper_yellow = np.array([33,255,255])
yellow_mask = cv2.inRange(hsv,lower_yellow,upper_yellow)

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
red_mask = cv2.inRange(hsv,lower_red,upper_red)

contours_b,_ = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours_y,_ = cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours_r,_ = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours_b:
    area = cv2.contourArea(contour)
    if area>100:
        cv2.drawContours(img,contour,-1,(0,255,0),3)
        bounding_box = cv2.boundingRect(contour)
        cv2.line(img,(bounding_box[0],bounding_box[1]),(bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]),3)
        print("Blue Coordinate = ",bounding_box[0]+bounding_box[2]/2,bounding_box[1]+bounding_box[3]/2)
        
for contour in contours_r:
    area = cv2.contourArea(contour)
    if area>100:
        cv2.drawContours(img,contour,-1,(0,255,0),3)
        bounding_box = cv2.boundingRect(contour)
        cv2.line(img,(bounding_box[0],bounding_box[1]),(bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]),3)
        print("Red Coordinate = ",bounding_box[0]+bounding_box[2]/2,bounding_box[1]+bounding_box[3]/2)
for contour in contours_y:
    area = cv2.contourArea(contour)
    if area>100:
        cv2.drawContours(img,contour,-1,(0,255,0),3)
        bounding_box = cv2.boundingRect(contour)
        cv2.line(img,(bounding_box[0],bounding_box[1]),(bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]),3)
        print("Yellow Coordinate = ",bounding_box[0]+bounding_box[2]/2,bounding_box[1]+bounding_box[3]/2)

cv2.imshow('image',img)
#cv2.imshow('blue_mask',blue_mask)
#cv2.imshow('yellow_mask',yellow_mask)
#cv2.imshow('red_mask',red_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
