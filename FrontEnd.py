import pygame as pg
from backend import randomshape2,find_res_of_list

from random import randint
from time import time
import pygame_widgets as pgw
from pygame_widgets.slider import Slider


scrlen=650#700 is bigger than my screen. 650 works fine. 

def random_color():return randint(0,256),randint(0,256),randint(0,256)

screen=pg.display.set_mode((scrlen,scrlen))

clock=pg.time.Clock()

def draw_list(list1,color):
    resolution=(find_res_of_list(list1))+2
    unit=scrlen/resolution
    for n in list1:
        actual_x=(n[0]+resolution/2)*unit-unit/2
        actual_y=(n[1]+resolution/2)*unit-unit/2
        pg.draw.rect(screen,color,pg.Rect(actual_x,actual_y,unit+1,unit+1))

col=random_color()

def darker_color(color):return 0.7*color[0],0.7*color[1],0.7*color[2]



def time_passed(basetime):return time()-basetime

def run(freq):
    pg.init()

    slider=Slider(screen,10,int(0.9*scrlen),scrlen-20,20,min=1,max=49,step=1)#These numbers aren't perfect. I could work a bit on that. 
    count = 0

    
    while True: 
        a=pg.event.get()
        for event in a:
            if event.type==pg.QUIT:
                pg.quit()
                exit()
            
        if count%freq==0:#There is someshit with count that I do not understand. 
            screen.fill((0,0,0))
            draw_list(randomshape2(slider.getValue()),random_color())
        count +=1
        pgw.update(a)
        pg.display.update()#It still runs as I want it too though. 

        clock.tick(20)
run(30)