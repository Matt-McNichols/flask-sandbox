from Tkinter import *
import pyperclip


# TODO: 
# add cmd function
# add change row function to cmd

class eightKey(Frame):
  def __init__(self,master):
    self.f = Frame.__init__(self, master)
    self.master=master

    self.row=0
    self.RL=''
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
      print t
      self.lOut.append(Label(self.f,width=12,height=2,text=t,bg='green'))

    # use grid to place labels
    for i in range(0,len(self.lOut)-1,2):
      self.lOut[i].grid(row=i,column=0)
      self.lOut[i+1].grid(row=i,column=1)

    # change color of starting row to white 
    self.lOut[self.row].config(bg='white')
    self.lOut[self.row+1].config(bg='white')

    # create event callbacks
    self.master.bind('<KeyPress>',self.keyDown)
    self.master.bind('<KeyRelease>',self.keyUp)


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

    # define output text label
    self.textOut = Label(self.f,width=12,text='',bg='light blue')
    self.textOut.grid(columnspan=2)

    self.cPrime=None
    self.cSec=None
    self.isCMD=False
    self.isHold=''

    return  

  # 3 options
  # * cPrimeDown -- cPrimeUp
  # * cPrimeDown -- cSecDown -- cPrimeUp -- cSecUp
  # * cPrimeDown -- cSecDown -- cSecUp -- cPrimeUp
  def keyDown(self,event):
    if not self.cPrime:
      self.cPrime=event.char
    else:
      self.cSec=event.char


  def keyUp(self,event):
    if self.cPrime is event.char:
      if self.isCMD:
        self.cPrime=None
        self.isCMD=False
        return
      if not self.cSec:
        #print 'INSERT({0})'.format(self.cPrime)
        self.INS()
        self.cPrime=None
      else:
        ## quick typing will stagger up/down (pdown/sdown/pup/sup)
        ##print 'INSERT({0})'.format(self.cPrime)
        #self.INS()
        self.CMD()
        self.cPrime=None
        self.cSec=None
    if self.cSec is event.char:
      print 'CMD({0},{1})'.format(self.cPrime,self.cSec)
      self.CMD()
      self.cSec=None
      #self.cPrime=None
      self.isCMD=True

  def INS(self):
    cTmp=self.keyDict[self.cPrime][self.row/2]
    txtTmp=self.textOut.cget('text')
    # check for key hold
    if len(txtTmp) > 2:
      if txtTmp[-1] is cTmp and txtTmp[-2] is cTmp:
        # assume key hold 
        self.textOut.config(text=txtTmp[0:-2])
        # set hold flag
        self.isHold=cTmp
        return
    if self.isHold is '':
      self.textOut.config(text=txtTmp+cTmp)
    elif self.isHold != cTmp:
      self.isHold=''
      self.textOut.config(text=txtTmp+cTmp)

  def CMD(self):
    if self.cPrime is 'f' and self.cSec is 'j':
      print 'space'
      txtTmp=self.textOut.cget('text')
      self.textOut.config(text=txtTmp+' ')
    elif self.cPrime is 'j' and self.cSec is 'f':
      print 'backspace'
      txtTmp=self.textOut.cget('text')
      self.textOut.config(text=txtTmp[0:-1])
    elif self.cPrime is 'a' and self.cSec is ';':
      # copy
      self.copy()
    elif self.cPrime is ';' and self.cSec is 'a':
      # cut
      self.cut()
    elif self.cPrime is 'k':
      self.lOut[self.row].config(bg='green')
      self.lOut[self.row+1].config(bg='green')
      # change row 
      if self.cSec is 'f':
        self.row=0
      elif self.cSec is 'd':
        self.row=2
      elif self.cSec is 's':
        self.row=4
      elif self.cSec is 'a':
        self.row=6
      self.lOut[self.row].config(bg='white')
      self.lOut[self.row+1].config(bg='white')
      
  def copy(self):
    print 'copy: {0}'.format(self.textOut.cget("text"))
    pyperclip.copy(self.textOut.cget("text"))

  def cut(self):
    self.copy()
    self.textOut.config(text='')
  
root = Tk()
eightKeyInst=eightKey(root)
mainloop()
