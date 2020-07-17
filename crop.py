import numpy as np
import cv2
from imutils import face_utils
import dlib
    
predictor = dlib.shape_predictor('data/shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()

# load image
img = cv2.imread('data/original/0.jpg',1)       
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
            
# detect kp
rects = detector(gray, 0)
shape = predictor(gray, rects[0])
shape = face_utils.shape_to_np(shape)      
shape = np.round(shape)
      
# draw mask 
msk = np.zeros(img.shape, dtype=np.uint8)
cv2.fillPoly(msk, [cv2.convexHull(shape)], (1,1,1))
       
# crop & resize
umin = np.min(shape[:,0]) 
umax = np.max(shape[:,0])
vmin = np.min(shape[:,1]) 
vmax = np.max(shape[:,1])
          
umean = np.mean((umin,umax))
vmean = np.mean((vmin,vmax))
                  
l = round( 1.2 * np.max((umax-umin,vmax-vmin)))
      
if (l > np.min(img.shape[:2])):
    l = np.min(img.shape[:2])
        
us = round(np.max((0,umean-float(l)/2)))
ue = us + l
    
vs = round(np.max((0,vmean-float(l)/2))) 
ve = vs + l
            
if (ue>img.shape[1]):
    ue = img.shape[1]
    us = img.shape[1]-l
    
if (ve>img.shape[0]):
    ve = img.shape[0]
    vs = img.shape[0]-l
                
us = int(us)
ue = int(ue)  
      
vs = int(vs)
ve = int(ve)    
      
img = cv2.resize(img[vs:ve,us:ue],(256,256))
msk = cv2.resize(msk[vs:ve,us:ue],(256,256),interpolation=cv2.INTER_NEAREST)
      
# save images 
cv2.imwrite('data/cropped/0.jpg', img)
cv2.imwrite('data/cropped/0_msk.jpg', msk * 255)