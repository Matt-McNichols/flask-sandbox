from Tkinter import *

class mKeyboard(Frame):
  def __init__(self,master):
    self.f = Frame.__init__(self, master)
    self.master=master
    self.mode=0
    self.row=None
    self.alt=False
    self.keyHome ='a s d f g h j k l ;'
    self.keyD ='z x c v b n m , . /'
    self.keyU ='q w e r t y u i o p'
    self.symHome ='1 2 3 4 5 6 7 8 9 0'
    self.symD ='1 2 3 4 5 6 7 8 9 0'
    self.symU ='1 2 3 4 5 6 7 8 9 0'
    self.lOutText=self.keyHome
    self.lOut = Label(self,text=self.lOutText, width=12, bg='green' )
    self.lOut.pack(side=LEFT, padx=2, pady=2)
    self.master.bind('<Key>',self.keyDown)
    self.master.bind('<ButtonPress>',self.butDown)
    #self.master.bind('<Alt>',self.alt)
    
    self.keyDict = {'a':('q','z'),
    's':('w','x'),
    'd':('e','c'),
    'f':('r','v'),
    'g':('t','b'),
    'h':('y','n'),
    'j':('u','m'),
    'k':('i',','),
    'l':('o','.'),
    ';':('p','/'),
    }
    
    self.symDict = {'a':('1'),
    's':('2'),
    'd':('3'),
    'f':('4'),
    'g':('5'),
    'h':('6'),
    'j':('7'),
    'k':('8'),
    'l':('9'),
    ';':('0'),
    }
    
    self.pack(fill=X)


  def keyDown(self,event):
    #print event.keycode
    #print self.mode, self.row
    
    if event.char in self.keyDict.keys():

      if self.mode is 0:
        print 'no mode selected'

      elif self.mode is 1:
        if self.row is None:
          print '{0}'.format(event.char)
        elif self.row is 'up':
          print '{0}'.format(self.keyDict[event.char][0])
        elif self.row is 'down':
          print '{0}'.format(self.keyDict[event.char][1])

      elif self.mode is 3:
        if self.row is None:
          print '{0}'.format(self.symDict[event.char][0])
        elif self.row is 'up':
          print '{0}'.format(self.symDict[event.char][0])
        elif self.row is 'down':
          print '{0}'.format(self.symDict[event.char][0])
      else:
        print 'error'


  def butDown(self,event):
    print event.num
    # 1 (left click) is letter mode
    # 3 (right click) is symbol mode
    if event.num is 1:
      self.mode=1
      self.row=None
      self.lOut.configure(text=self.keyHome)
    if event.num is 3:
      self.mode=3
      self.row=None
      self.lOut.configure(text=self.symHome)

    # 4 (scroll up) set row to up
    # 5 (scroll down) set row to down
    if event.num is 4:
      self.row='up'
      if self.mode is 1:
        self.lOut.configure(text=self.keyU)
      elif self.mode is 3:
        self.lOut.configure(text=self.symU)
    if event.num is 5:
      self.row='down'
      if self.mode is 1:
        self.lOut.configure(text=self.keyD)
      elif self.mode is 3:
        self.lOut.configure(text=self.symD)
    return



root = Tk()
mKeyboardTest=mKeyboard(root)
mainloop()
