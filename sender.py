import socket
import Image
import PIL
from PIL import Image
import ImageDraw
import ImageFilter
from PIL import ImageGrab
#from VideoCapture import Device
#cam = Device()
#cam.setResolution(320,240)
clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisocket.connect(("192.168.8.123", 1234))
W = 800
H = 600
bkgd = Image.new("RGB",(W,H), (255,255,255))
while 1:
    #im = cam.getImage()
    im = ImageGrab.grab();
    width, height = im.size
    #print width, height
    #print width/800.0, height/600.0
    rate = max(width/800.0, height/600.0)
    rewidth = int(width/rate)
    reheight = int(height/rate)
    print rewidth, reheight
    im = im.resize((rewidth,reheight), Image.ANTIALIAS)
    box = ((W- rewidth)/2, (H- reheight)/2)
    bkgd.paste(im, box )
    #bkgd.show()
    da = bkgd.tostring()
    #print len(da)
    clisocket.send(da)
    #print "Hello"
#s.close()