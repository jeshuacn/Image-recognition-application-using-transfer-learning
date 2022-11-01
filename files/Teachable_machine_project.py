import cv2
from keras.models import load_model
import numpy as np
import mediapipe as mp
import serial
import time
from pygame import mixer
import tkinter as tk
from tkinter import messagebox as mb


mp_face_detection = mp.solutions.face_detection

# Teachable machine model
model = load_model('keras_model.h5')

# Camera
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Loading files with labels
with open('labels.txt','r') as f:
    class_names = f.read().split('\n') 

LABELS = ["With Mask", "Without Mask"]

# Conection to arduino
try:
    arduino = serial.Serial('COM3',9600)
    time.sleep(2)
except:
    # IF Arduino is not detected show a warning
    root = tk.Tk()
    root.withdraw()
    mb.showwarning("Alert","You must plug the Arduino into the USB port")
    quit()

# Initialize module of pygame
mixer.init()

data = np.ndarray(shape = (1,224,224,3), dtype = np.float32) #  array multidimentional that recieve the model

i = 0
with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:

    while True:
      ret, frame = cap.read()
      if ret == False: break
      frame = cv2.flip(frame,1) # For the camera to reflect as a mirror
      
      resized_frame = cv2.resize(frame,(224,224), interpolation= cv2.INTER_AREA) # resizing the input image
      image_np = np.array(resized_frame)
    
      normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # normalize the image
      data[0] = normalized_image
      prediction = model.predict(data) # prediction
    
      # face detection
      height, width, _ = frame.shape
      frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      results = face_detection.process(frame_rgb)

      if results.detections is not None:
          for detection in results.detections:
              xmin = int(detection.location_data.relative_bounding_box.xmin * width)
              ymin = int(detection.location_data.relative_bounding_box.ymin * height)
              w = int(detection.location_data.relative_bounding_box.width * width)
              h = int(detection.location_data.relative_bounding_box.height * height)
              if xmin < 0 and ymin < 0:
                  continue
            
              index = np.argmax(prediction)
              class_name = LABELS[index]
              confidence_score = prediction[0][index]
              
              i+=1
              if i == 50:
                 print('Class:', class_name)
                 print('Confidence score',confidence_score)

                 if prediction[0][1] > 0.5:
                    # if the model detects that the person is not wearing mask, play the audio
                    sound = mixer.Sound('Colocar_mascarilla.mp3')
                    sound.play()
                 else:
                     sound.stop()
                 i = 0
              
              cv2.putText(frame,"{}".format(class_name),(xmin,ymin -5), 1, 1.3, (255, 255, 255), 2, cv2.LINE_AA)
              cv2.putText(frame,"Confidence Score:,{:0.2f}".format(confidence_score),(xmin,ymin -25), 1, 1.3, (255, 255, 255), 1, cv2.LINE_AA)

              if class_name == "With Mask":
                # Turn on Blue LED color in the arduino
                  arduino.write(b'p')
              else:
                # Turn on Red LED in the arduino
                  arduino.write(b'n')



      cv2.imshow("Frame",frame)
      k = cv2.waitKey(1)
      if k ==27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.write(b'e')
arduino.close()
mixer.quit()
