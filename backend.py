from random import randint

def chance(odds):
    return odds>randint(0,100)

def check_and_input(x,y,odds,thelist):
    if (x,y) not in thelist: 
            if chance(odds):
                thelist.append((x,y))

class Square:
    
    def __init__(self,x,y,odds,thelist):#I used to have self.x and self.y defined here but I don't need it for now.
        check_and_input(x+1,y,odds,thelist)#I'll probably need it for future challenges. 
        check_and_input(x,y+1,odds,thelist)#I am pretty sure that I do not need to have this as a class but fuck it. 
        check_and_input(x-1,y,odds,thelist)
        check_and_input(x,y-1,odds,thelist)

def randomshape(odds):#
    shape=[(0,0)]
    for n in shape:#These two lines should be made into a function. 
        Square(n[0],n[1],odds,shape)#I use the for n in list as a queue data structure. 
    if shape==[(0,0)]:
        shape=randomshape(odds)
    return shape

def randomshape2(odds):
    shape=[(0,0)]
    while shape==[(0,0)]:
        for n in shape:
            Square(n[0],n[1],odds,shape)
    return shape


def find_res_of_list(mylist):
    x_top=x_bot=y_top=y_bot=0 
    for n in mylist:
        x_top=max(abs(n[0]),x_top)
        x_bot=min(abs(n[0]),x_bot)
        y_top=max(abs(n[1]),y_top)
        y_bot=min(abs(n[1]),y_bot)
    return 2*max(x_top,x_bot,y_top,y_bot)#I need to fix this function just a little bit. 

def find_centers_list(mylist):
    x_top=x_bot=y_top=y_bot=0 
    for n in mylist:
        x_top=max(abs(n[0]),x_top)#centeredlist() uses this function and it doesn't work in pygamedemo
        x_bot=min(abs(n[0]),x_bot)
        y_top=max(abs(n[1]),y_top)
        y_bot=min(abs(n[1]),y_bot)
    return (x_top+x_bot)/2,(y_top+y_bot)/2

def centeredlist(list1):
    minus=find_centers_list(list1)
    for ind in range(len(list1)):
        list1[ind]=((list1[ind][0]-minus[0],list1[ind][1]-minus[1]))
    return list1#This one doesn't work in the pygamedemo.py

