import cv2

# THIS IS WEBCAM
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()     # READING FROM WEBCAM
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):       # PRESS 'Q' TO SAVE IMAGE
            cv2.imwrite('image.jpg', back) 
            break                            # AFTER SAVING BREAK

cap.release()
cv2.destroyAllWindows()