From RaspberryPi Website
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1


from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

#You can rotate the image by 90, 180, or 270 degrees. To reset the image, set rotation to 0 degrees.
#camera.rotation = 180

#Make the camera preview see-through by setting an alpha level,The alpha value can be any number between 0 and 255,the default alpha level could be 250
#camera.start_preview(alpha=200)

"""
 Take a still picture'
   camera.start_preview()
    #it’s important to sleep for at least two seconds before capturing an image, because this gives the camera’s sensor time to sense the light levels.
   sleep(5)
  camera.capture('/home/pi/Desktop/20220421.jpg')
"""

"""
#Take a loop picture'
#a loop to take five pictures in a row:

camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
"""

"""
#Recording video with Python code
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
"""

"""
#Set the image resolution
#By default, the image resolution is set to the resolution of your monitor. The maximum resolution is 2592×1944 for still photos, and 1920×1080 for video recording.Note: you also need to set the frame rate to 15 to enable this maximum resolution.

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
"""

"""
#Add text to your image
camera.start_preview()
camera.annotate_text = "Hello Chunfa!"
#You can set the text size to anything between 6 to 160. The default size is 32.
camera.annotate_text_size = 160
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()
"""

"""
#It’s also possible to change the text colour.
#add Color to your import line at the top of the program:from picamera import PiCamera, Color
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
"""

"""
#Change the brightness of the preview
#The default brightness is 50, and you can set it to any value between 0 and 100.
camera.start_preview()
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()
"""

"""
#The following loop adjusts the brightness and also adds text to display the current brightness level:
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()
"""

"""
#Change the contrast of the preview
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
"""

#Add cool image effects
#You can use camera.image_effect to apply a particular image effect.
"""
The image effect options are:
none
negative
solarize
sketch
denoise
emboss
oilpaint
hatch
gpen
pastel
watercolor
film
blur
saturation
colorswap
washedout
posterise
colorpoint
colorbalance
cartoon
deinterlace1
deinterlace2
The default effect is none.
"""

"""    
# 1 coloreffect
camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()
"""

"""
#loop over all the image effects with camera.IMAGE_EFFECTS:
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    #camera.capture('/home/pi/Desktop/image%s.jpg' % effect)
    sleep(5)
camera.stop_preview()
"""

#Set the image exposure mode
"""
The exposure mode options are:

off
auto
night
nightpreview
backlight
spotlight
sports
snow
beach
verylong
fixedfps
antishake
fireworks
The default mode is auto.
"""

"""
#loop over all the image effects with camera.IMAGE_EFFECTS:
camera.start_preview()
for mode in camera.EXPOSURE_MODES:
    camera.exposure_mode = mode
    camera.annotate_text = "Mode: %s" % mode
#camera.exposure_mode = 'beach'
    sleep(5)
#camera.capture('/home/pi/Desktop/beach.jpg')
camera.stop_preview()
"""

#Change the image white balance
"""
ou can use camera.awb_mode to set the auto white balance to a preset mode.

The available auto white balance modes are:

off
auto
sunlight
cloudy
shade
tungsten
fluorescent
incandescent
flash
horizon
The default is auto.
"""


#Sunlight mode
camera.start_preview()
camera.awb_mode = 'fluorescent'
sleep(5)
camera.capture('/home/pi/Desktop/fluorescent.jpg')
camera.stop_preview()

"""
#loop over all the auto white balance modes with camera.AWB_MODES,

camera.start_preview()
for mode in camera.AWB_MODES:
    camera.exposure_mode = mode
    camera.annotate_text = "Mode: %s" % mode
    sleep(5)
camera.stop_preview()
"""






  
  
  












