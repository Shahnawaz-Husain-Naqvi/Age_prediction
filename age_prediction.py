import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2LUV)
    try:

        result = DeepFace.analyze(frame, actions = ['age'])
        age = round(result[0]['age'])
        age_text = f"Age: {age}"
    except:
        age_text = "Age: N/A"
    cv2.putText(frame,age_text,(0,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)


    cv2.imshow('window',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()       

