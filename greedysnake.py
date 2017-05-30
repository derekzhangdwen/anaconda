from tkinter import *
import random
import time

root = Tk(className='greedy snake')
root.geometry("300x400+100+100")
root.maxsize(300,400)
root.minsize(300,400)

for t in range(30):
    for i in range(40):
        locals()['frames'+str(t)+str(i)]=Frame(width=10,height=10,bg='black')
        locals()['frames'+str(t)+str(i)].grid(row=i,column=t)

def keypress(event):
    orient(event.char)

bodies=[]
length=0
def newbody(name,y1,x1,y2,x2,wid,hei,stick1,stick2):
    global length
    global bodies
    globals()['bodya'+name]=Frame(width=wid,height=hei,bg='white')
    globals()['bodya'+name].grid(row=x1,column=y1,sticky=stick1)
    globals()['bodyb'+name]=Frame(width=wid,height=hei,bg='white')
    globals()['bodyb'+name].grid(row=x2,column=y2,sticky=stick2)
    length=length+1
    #print(bodies)
    bodies.append((y1,x1))

ori='d'
turned=False
def orient(char):
    global ori
    global turned
    if (((ori=='a' or ori=='d')and(char=='w' or char=='s'))or((char=='a' or char=='d')and(ori=='w' or ori=='s')))and turned:
        turned=False
        ori=char
    #if(char=='j'):
        #newbody(str(length),0,0,0,0,0,0,'E','W')

for t in range(2):
    newbody(str(length),t,3,t+1,3,8,6,'E','W')

    
reddot=Frame(width=6,height=6,bg='red')
def randomp():
    global bodies
    #print(bodies)
    index=[]
    for t in range(2,28):
        for i in range(2,38):
            if (t,i) not in bodies:
                index.append((t,i))
    return random.choice(index)

rcol=0
rrow=0
def mover():
    global rcol
    global rrow
    global reddot
    rcol=randomp()[0]
    rrow=randomp()[1]
    reddot.grid(row=rrow,column=rcol)
mover()   



tail=0
nextx=1
nexty=3
def eachm(name,y1,x1,y2,x2,wid,hei,stick1,stick2):   
    globals()['bodya'+name]['width']=wid
    globals()['bodya'+name]['height']=hei           
    globals()['bodyb'+name]['width']=wid
    globals()['bodyb'+name]['height']=hei
    globals()['bodya'+name].grid(row=y1,column=x1,sticky=stick1)
    globals()['bodyb'+name].grid(row=y2,column=x2,sticky=stick2)
    bodies.append((x1,y1))
    del bodies[0]

def move():
    global tail
    global nextx
    global nexty
    global turned
    global bodies
    global length
    global ori
    temp=True
    for t in range(len(bodies)-1):
        if bodies[t]==(nextx,nexty):
            temp=False
    if (nextx,nexty)==(rcol,rrow):
        mover()
        newbody(str(length),30,0,30,0,0,0,'E','W')
    if 0<nextx<29 and 0<nexty<39 and temp:
        if ori=='d':
            eachm(str(tail),nexty,nextx,nexty,nextx+1,8,6,'E','W')
            nextx=nextx+1           
        elif ori=='w':
            eachm(str(tail),nexty,nextx,nexty-1,nextx,6,8,'N','S')
            nexty=nexty-1
        elif ori=='s':
            eachm(str(tail),nexty,nextx,nexty+1,nextx,6,8,'S','N')
            nexty=nexty+1
        elif ori=='a':
            eachm(str(tail),nexty,nextx,nexty,nextx-1,8,6,'W','E')
            nextx=nextx-1
        turned=True
        tail=(tail+1)%(length)
        root.after(100,move)
    else:
        
        print(length)
        for t in range(length):
            globals()['bodya'+str(t)].destroy()
            globals()['bodyb'+str(t)].destroy()
        tail=0
        length=0
        nextx=1
        nexty=3
        bodies=[]
        turned=False
        ori='d'
        for t in range(2):
            
            newbody(str(length),t,3,t+1,3,8,6,'E','W')
        time.sleep(2)    
        root.after(0,move)
        #root.destroy()
        #root = Tk(className='test')
        #print(t)

keylistener=Frame(bg='black')
keylistener.grid(row=0,column=0)
keylistener.bind('<Key>',keypress)
keylistener.focus_force()
#root.after(1, lambda: root.focus_force())
root.attributes("-topmost", True)
#root.after(0,test1)
root.after(0,move())

root.mainloop()
