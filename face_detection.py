import cv2
index=0
print(index)
cap = cv2.VideoCapture(index)
while True:
    ret, frame = cap.read()
    print("read")
    if ret:
        print("imshow")
        cv2.imshow("Webcam Output", frame)
    else:
        break
    key = cv2.waitKey(10)  & 0xFF
    if key == 27:# or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1.0: 
        break
cv2.destroyAllWindows()