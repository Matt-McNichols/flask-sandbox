from Tkinter import *

class mKeyboard(Frame):
  def __init__(self,master):
    self.f = Frame.__init__(self, master)
    self.master=master
    self.row=0
    self.RL=''
    # define row of chars
    self.charRows=[('a','o','e','u'),
                   ('h','t','n','s'),
                   ('i','d','p','y'),
                   ('f','g','c','r'),
                   ('l','q','j','k'),
                   ('x','b','m','w'),
                   ('v','z','-','?'),
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

    self.textOut = Entry(self.f)
    self.textOut.insert('end','test')
    self.textOut.grid(columnspan=2)

    self.bEraseAll = Button(self.f, text='Erase All',height=1, command=self.eraseAll)
    self.bEraseAll.grid(row=0, column=2)

    return  


  def eraseAll(self):
    print 'erase all'
    self.textOut.delete(0,'end')

  def moveRow(self,char):
    #print 'moveRow'
    if self.RL == '':
      print self.keyDict[char][self.row/2]
      self.textOut.insert('end',self.keyDict[char][self.row/2])
    elif self.RL == 'R':
      self.lOut[self.row].config(bg='green')
      self.lOut[self.row+1].config(bg='green')
      if char == 'a':
          self.row=0
          self.lOut[self.row].config(bg='white')
          self.lOut[self.row+1].config(bg='white')
      if char == 's':
          self.row=2
          self.lOut[self.row].config(bg='white')
          self.lOut[self.row+1].config(bg='white')
      if char == 'd':
          self.row=4
          self.lOut[self.row].config(bg='white')
          self.lOut[self.row+1].config(bg='white')
      if char == 'f':
          self.row=6
          self.lOut[self.row].config(bg='white')
          self.lOut[self.row+1].config(bg='white')


  def keyDown(self,event):
    # check if key is valid 
    #print 'down: {0}'.format(event.char)
    if event.char == 'n':
      self.RL='R'
    elif event.char == 'v':
      self.RL='L'
    elif event.char in self.keyDict.keys():
      self.moveRow(event.char)

  def keyUp(self,event):
    #print 'up: {0}'.format(event.char)
    if event.char == 'n':
      self.RL=''
    elif event.char == 'v':
      self.RL=''






root = Tk()
mKeyboardTest=mKeyboard(root)
mainloop()













#  def keyDownOld(self,event):
#    #print event.keycode
#    #print self.mode, self.row
#    
#    if event.char in self.keyDict.keys():
#
#      if self.mode is 0:
#        print 'no mode selected'
#
#      elif self.mode is 1:
#        if self.row is None:
#          print '{0}'.format(event.char)
#        elif self.row is 'up':
#          print '{0}'.format(self.keyDict[event.char][0])
#        elif self.row is 'down':
#          print '{0}'.format(self.keyDict[event.char][1])
#
#      elif self.mode is 3:
#        if self.row is None:
#          print '{0}'.format(self.symDict[event.char][0])
#        elif self.row is 'up':
#          print '{0}'.format(self.symDict[event.char][0])
#        elif self.row is 'down':
#          print '{0}'.format(self.symDict[event.char][0])
#      else:
#        print 'error'

#  def butDown(self,event):
#    print event.num
#    # 1 (left click) is letter mode
#    # 3 (right click) is symbol mode
#    if event.num is 1:
#      self.mode=1
#      self.row=None
#      self.lOut.configure(text=self.keyHome)
#    if event.num is 3:
#      self.mode=3
#      self.row=None
#      self.lOut.configure(text=self.symHome)
#
#    # 4 (scroll up) set row to up
#    # 5 (scroll down) set row to down
#    if event.num is 4:
#      self.row='up'
#      if self.mode is 1:
#        self.lOut.configure(text=self.keyU)
#      elif self.mode is 3:
#        self.lOut.configure(text=self.symU)
#    if event.num is 5:
#      self.row='down'
#      if self.mode is 1:
#        self.lOut.configure(text=self.keyD)
#      elif self.mode is 3:
#        self.lOut.configure(text=self.symD)
#    return
