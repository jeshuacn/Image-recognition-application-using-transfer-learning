# Image Recognition Application Using Transfer-learning
This is a project of image recognition using transfer learning using [Teachable Machine](https://teachablemachine.withgoogle.com/) from Google, to detect if a person is wearing a mask or not
and depending on the outcome it will turn on a red or blue LED, using an Arduino and Python.

## The model

This project was made using Teachable Machine to train the model. We used a dataset of 200 photos for each category.

Here we have two [labels](https://github.com/jeshuacn/Image-recognition-application-using-transfer-learning/blob/main/files/labels.txt):

  0 - mask
  
  1 - without mask
  
If the model detects that the person is not wearing a mask it will play an audio warning instructing the person to put on the mask.

This audio is in Spanish. [MP3](https://github.com/jeshuacn/Image-recognition-application-using-transfer-learning/blob/main/files/Colocar_mascarilla.mp3)
 
## Arduino


Here is the Arduino [script](https://github.com/jeshuacn/Image-recognition-application-using-transfer-learning/blob/main/files/encender_leds.ino) used to turn the LEDs ON and OFF

Here's the circuite we used with the arduino:

![image](https://user-images.githubusercontent.com/33787097/199165010-8f0e3150-4d1c-486e-ad9b-4c347e5c90fb.png)
Image from: https://thecustomizewindows.com/2018/07/arduino-blink-two-leds-alternatively/

## Python script

Here is the Python program for this application of image detection using OpenCV to capture images from the webcam in real-time.

[Python Script](https://github.com/jeshuacn/Image-recognition-application-using-transfer-learning/blob/main/files/Teachable_machine_project.py)
