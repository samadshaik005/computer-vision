import cv2

cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('save_output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened()) #to check opend/not ---/true/false


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True: #ret is boolean
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    #to show width height of frame
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame) #save the video

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()