import cv2

#part1 read and show image

img=cv2.imread('C:\\Users\\Herin\\OneDrive\\Pictures\\walliper\\TXT-.jpg')
cv2.imshow('Main image', img)

#part 2 resize and convert to gray scail

resized=cv2.resize(img,(380,300))


gray= cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray picture' , gray)


#part 3 Edge detection 

edges =cv2.Canny(gray,100,200)
cv2.imshow('Ditect Edges', edges)

#part4 Ditection with shape and write text

ditect=cv2.rectangle(resized, (88,58), (302,130), (80,0,100),5)

ditect= cv2.putText(resized, ('Tomorrow X Together'),(100,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,0,100), 2 ,cv2.LINE_AA)
cv2.imshow('texted', ditect)

cv2.imwrite('changed.png',ditect)

cv2.waitKey(0)
cv2.destroyAllWindows()