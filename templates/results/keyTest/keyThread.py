from tkinter import *
import pyperclip
import keyboard
import sys
import threading

# TODO: 
# add cmd function
# add change row function to cmd

class homeKey(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def quit(self):
        self.root.quit()

    def run(self):
        self.root=Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quit())

        self.row=0
        # define row of chars
        self.charRows=[('e','t','a','o'),
                        ('i','n','s','h'),
                        ('r','d','l','c'),
                        ('u','m','w','f'),
                        ('g','y','p','b'),
                        ('v','k','j','x'),
                        ('q','z','-','?'),
                        ('<','>','+','"')
                    ]

        # define 8 fingers 
        self.fingers= ['a','s','d','f','j','k','l',';']

        # create labels
        self.lOut = []
        for i in range(len(self.charRows)):
            row=self.charRows[i]
            t=''
            for i in range(len(row)):
                char = row[i]
                t = t+' '+char+' '
            print (t)
            self.lOut.append(Label(self.root,width=12,height=2,text=t,bg='green'))

        # use grid to place labels
        for i in range(0,len(self.lOut)-1,2):
            self.lOut[i].grid(row=i,column=0)
            self.lOut[i+1].grid(row=i,column=1)


        fingerChars = []
        for i in range(0,len(self.charRows)-1,2):
            tmpR=self.charRows[i]
            tmpR1=self.charRows[i+1]
            fingerChars.append(tmpR+tmpR1)

        # define 8 fingers and keys they map to
        self.keyDict={}
        for f in range(len(self.fingers)):
            tmpList=[]
            for cList in fingerChars:
                tmpList.append(cList[f])
                self.keyDict[self.fingers[f]]=tmpList

        self.cListLh = []
        self.cListRh = []
        self.isCMD   = False
        self.upHand  = None
        self.root.mainloop()

        return  

    # 3 options
    # * cPrimeDown -- cPrimeUp
    # * cPrimeDown -- cSecDown -- cPrimeUp -- cSecUp
    # * cPrimeDown -- cSecDown -- cSecUp -- cPrimeUp
    #
    #self.lOut[self.row].config(bg='green')
    # lh rows 0,2,4,6
    #self.row=2*(len(self.cListLh))
    #self.lOut[self.row].config(bg='white')

    def keyDown(self,event):
        if event.name == 'esc':
            keyboard.unhook_all()
            sys.exit()
        elif event.name in self.fingers[0:4] :
            if event.name not in self.cListLh:
                self.cListLh.append(event.name)
        elif event.name in self.fingers[4:7]:
            if event.name not in self.cListRh:
                self.cListRh.append(event.name)

        if (len(self.cListLh) is 1 and len(self.cListRh) is 0) or (len(self.cListLh) is 0 and len(self.cListRh) is 1):
            self.isCMD = True
        else:
            self.isCMD = False

        print ('down: {0}   isCMD: {1}'.format(event.name,self.isCMD))

    # TODO
    def keyUp(self,event):
        self.upHand = None
        if event.name in self.fingers[0:4] :
            self.upHand = 'L'
        elif event.name in self.fingers[4:7] :
            self.upHand = 'R'
        print ('upChar: {0}   upHand: {1}'.format(event.name,self.upHand))
        self.keyClear()


    
    def keyClear(self):
        self.lOut[self.row].config(bg='green')
        self.lOut[self.row+1].config(bg='green')
        self.row=0
        self.cListRh = []
        self.cListLh = []


    def INS(self,key):
        cTmp=self.keyDict[key][int(self.row/2)]
        keyboard.send(cTmp)

    def copy(self):
        keyboard.send('ctrl+a, ctrl+c')

    def cut(self):
        keyboard.send('ctrl+a, ctrl+x')
        #self.copy()
        #self.textOut.config(text='')




def keyListen():
    def down(event):
        #keyboard.send("backspace")
        print('down: {0}'.format(event.name))

    def up(event):
        #keyboard.send("backspace")
        print('up: {0}'.format(event.name))
        if(event.name == 'esc'):
            print('esc -- kill')
            keyboard.unhook_all()
            sys.exit()

    keyboard.unhook_all()
    tkInst=homeKey()
    print("running after tk mainloop")
    keyboard.on_press(tkInst.keyDown,True)
    keyboard.on_release(tkInst.keyUp,True)
    #keyboard.on_press(down,True)
    #keyboard.on_release(up,True)
    keyboard.wait()




keyListen()
#root.after(0,keyListen)
#mainloop()





