#!usr/bin/python

import pygame, sys, os, math, netifaces, time
from pygame.locals import *

os.environ["SDL_FBDEV"] = "/dev/fb8"

FPS=20
DISPLAY_H=128
DISPLAY_W=128
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
IRED  = (176,  23,  21)

# main game loop
def main():
 global FPSCLOCK, DISPLAYSURF
 pygame.init()
 FPSCLOCK = pygame.time.Clock()
 DISPLAYSURF=pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
 pygame.mouse.set_visible(0)
 trip = 0
 while True:
  for event in pygame.event.get():
   if event.type ==  QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
    pygame.quit()
    sys.exit()
  if trip == 0:
   write_text("eth0",DISPLAYSURF)
   trip = 1
  else:
   write_text("wlan0",DISPLAYSURF)
   trip = 0
  pygame.display.update()
  FPSCLOCK.tick(FPS)
  time.sleep(10)

# multiline text rendering
def ml_text(surface, text, pos, font, color):
 words = [word.split(' ') for word in text.splitlines()]
 space = font.size(' ')[0]
 max_width, max_height = surface.get_size()
 x, y = pos
 for line in words:
  for word in line:
   word_surface = font.render(word, 0, color)
   word_width, word_height = word_surface.get_size()
   if x + word_width >= max_width:
    x = pos[0]
    y += word_height
   surface.blit(word_surface, (x, y))
   x += word_width + space
  x = pos[0]
  y += word_height

# a funtion to write text
def write_text(iface,surf):
 surf.fill(WHITE)
 addr=netifaces.ifaddresses(iface)
 fontObj = pygame.font.Font(None, 22)
 text = "N/A"
 if netifaces.AF_INET in addr:
  text = iface+"\nmac: "+addr[netifaces.AF_LINK][0]['addr']+"\nip_addr: "+addr[netifaces.AF_INET][0]['addr']
 else:
  text = iface+"\nmac: "+addr[netifaces.AF_LINK][0]['addr']+"\nip_addr: N/A"
 ml_text (surf,text,(6,6),fontObj, pygame.Color('black'))

# Run Main Function
if __name__ == '__main__':
 main()

