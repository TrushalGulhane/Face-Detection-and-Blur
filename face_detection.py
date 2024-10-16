import cv2
from mtcnn import MTCNN

cam =cv2.VideoCapture(0)
#video=cv2.imread('groupcnn1.jpeg')
detector =MTCNN()

while True:
    ret,video= cam.read()
    result=detector.detect_faces(video)

    for i in range(len(result)):
     if True:
        x,y,w,h= result[i]['box']                        
        video[y:y+h, x:x+w, :]=cv2.blur(video[y:y+h, x:x+w, :],(50,50))
        

     if True:


        #for face detection and draw rectangle
        x,y,w,h= result[i]['box']                        
        cv2.rectangle(video,(x,y),(x+w,y+h),(255,255,255),2)
        
     if False:

        #draw the landmark on face detection
        keypoint=result[i]['keypoints']

        left_eyex,left_eyey=keypoint['left_eye']
        right_eyex,right_eyey=keypoint['right_eye']
        nosex,nosey=keypoint['nose']
        left_mouthx,left_mouthy=keypoint['mouth_left']
        right_mouthx,right_mouthy=keypoint['mouth_right']

        cv2.circle(video,center=(left_eyex,left_eyey),color=(0,0,255),thickness=1,radius=2)
        cv2.circle(video,center=(right_eyex,right_eyey),color=(0,0,255),thickness=1,radius=2)
        cv2.circle(video,center=(nosex,nosey),color=(0,0,255),thickness=1,radius=2)
        cv2.circle(video,center=(left_mouthx,left_mouthy),color=(0,0,255),thickness=1,radius=2)
        cv2.circle(video,center=(right_mouthx,right_mouthy),color=(0,0,255),thickness=1,radius=2)


     

    cv2.imshow('window',video)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
     
cv2.destroyAllWindows()