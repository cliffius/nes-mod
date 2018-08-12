import sys
import serial
import time
from PIL import Image

ser = serial.Serial('/dev/serial0', 9600)
EndCom = "\xff\xff\xff"

def noBoxArt():
   if sys.argv[1] == "gb":
     ser.write('t1.txt="' + sys.argv[2] + '"' + EndCom)
     ser.write('p1.pic=2' + EndCom)
   elif sys.argv[1] == "gbc":
     ser.write('t1.txt="' + sys.argv[2] + '"' + EndCom)
     ser.write('p1.pic=3' + EndCom)
   elif sys.argv[1] == "gba":
     ser.write('t1.txt="' + sys.argv[2] + '"' + EndCom)
     ser.write('p1.pic=4' + EndCom)
   elif sys.argv[1] == "megadrive":
     ser.write('t1.txt="' + sys.argv[2] + '"' + EndCom)
     ser.write('p1.pic=5' + EndCom)
   elif sys.argv[1] == "nes":
     ser.write('t1.txt="' + sys.argv[2] + '"' + EndCom)
     ser.write('p1.pic=6' + EndCom)
   elif sys.argv[1] == "snes":
     ser.write('t1.txt="' + sys.argv[2] + '"' + EndCom)
     ser.write('p1.pic=7' + EndCom)
   else:
     ser.write('t1.txt=""' + EndCom)
     ser.write('p1.pic=1' + EndCom)

def get565(rgb):
   r = rgb[0]
   g = rgb[1]
   b = rgb[2]
   return ((r >> 3) << 11) + ((g >> 2) << 5) + (b >> 3)

# if exiting game
if sys.argv[1] == "END": 
   ser.write('t1.txt=""' + EndCom)
   ser.write('p1.pic=1' + EndCom)

# else if launching game
else:
   ser.write('cls 0' + EndCom) # clear screen

   # get image file name
   loc = "/opt/retropie/configs/all/emulationstation/downloaded_images/" + sys.argv[1] + "/"
   art = sys.argv[3][:-4] + "-image.jpg" # :-4 removes '.zip' from end of string
   size = 320, 240
   try: # try to get boxart
      cover_art = Image.open(loc + art)
      #cover_art = cover_art_orig.thumbnail(size)
   except: # if no box art, load text only
      noBoxArt()

   # loop through image one pixel at a time
   pixel_skip = 2
   for y in range(0, 240, pixel_skip): # screen height
      for x in range(0, 320, pixel_skip): # screen width
         rgb = cover_art.getpixel((x,y)) # get current pixel
         pix_color = get565(rgb) # convert to 565 decimal
         draw_string = 'fill ' + str(x) + ',' + str(y) + ',' + str(pixel_skip) + ',' + str(pixel_skip) + ',' + str(pix_color)
         ser.write(draw_string + EndCom)

   time.sleep(1)
   ser.close()
