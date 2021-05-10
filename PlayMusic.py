from datetime import datetime, date
import time
import pygame
import sys

pygame.init()
display=pygame.display.set_mode((400,300))
pygame.display.set_caption("sound demo")
while True:
    pygame.mixer.music.load("Water.mp3")
    soun_obj = pygame.mixer.Sound("Water.mp3")
    pygame.mixer.music.play()
    soun_obj.play()
    x=input("Have you take water yes or no :")
    if x==("yes").lower():
        exit()
fh1 = int(time.strftime("%H"))
fm1 = int(time.strftime("%M"))
if fh1 >= 9 and fm1 >= 00 and fh1 <= 16 and fm1 <= 59:
    print(fh1, fm1)
else:
    print(fh1, fm1)
    print(time.strftime("%H:%M"), datetime.now().time())

# start = datetime.now().time()
# time.sleep(3)
# end = datetime.now().time()
# print(start)
# print(end)
# print(datetime.combine(date.min, end) - datetime.combine(date.min, start))
