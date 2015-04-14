import socket
import Image
import os,sys,pygame
from pygame.locals import *

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("projector")
pygame.display.flip()

svrsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svrsocket.bind(("192.168.8.123", 1234))
svrsocket.listen(5);
svrhandler, addr = svrsocket.accept()


clock = pygame.time.Clock()    #frame rate
data = ""
while 1:
    try:
    	tmp = data
        while len(tmp) < width * height *3:
            tmp = tmp + svrhandler.recv(4096)
        data = tmp[0 : width*height*3]
        #print "Recv! Size: ", len(data)
        camshot = pygame.image.frombuffer(data, (width,height), "RGB")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(camshot, (0,0))
        pygame.display.update() 
        data = tmp[width * height * 3:len(tmp)]
        print clock.get_fps()     #frame rate
        clock.tick()
    except :
        print "Error!"
        exit(-1)