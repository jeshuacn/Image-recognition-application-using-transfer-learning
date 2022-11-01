# Image-recognition-application-using-transfer-learning
This is a project of image recognition using transfer learning using [Teachable Machine](https://teachablemachine.withgoogle.com/) from Google, to detect if a person is wearing a mask or not
and depending on the outcome it will turn on a red or blue LED, using an Arduino and Python.

## The model

This project was made using Teachable Machine to train the model. We used a dataset of 200 photos for each category.

Here we have two [labels](https://github.com/jeshuacn/Image-recognition-application-using-transfer-learning/blob/main/files/labels.txt):

  0 - mask
  
  1 - without mask
 
## Arduino


Here is the Arduino [script](https://github.com/jeshuacn/Image-recognition-application-using-transfer-learning/blob/main/files/encender_leds.ino) used to turn the LEDs ON and OFF

Here's the circuite we used with the arduino:

![image](https://user-images.githubusercontent.com/33787097/199165010-8f0e3150-4d1c-486e-ad9b-4c347e5c90fb.png)
https://thecustomizewindows.com/2018/07/arduino-blink-two-leds-alternatively/
