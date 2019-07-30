from Tkinter import *

class bKey(Frame):
  def __init__(self,master,idleText,enterText):
    Frame.__init__(self, master)
    self.bTextIdle=idleText
    self.bTextEnter=enterText
    #lOutText=''
    self.bKey = Button(self,text=self.bTextIdle, width=6 )
    self.bKey.bind('<Enter>',self.bEnter)
    self.bKey.bind('<Leave>',self.bLeave)
    self.bKey.bind('<Button-4>',self.sUp)
    self.bKey.bind('<Button-5>',self.sDown)

    #lOut = Label(f1,text=lOutText, width=6 )
    
    self.bKey.pack(side=LEFT, padx=2, pady=2)
    self.pack(fill=X)
    #lOut.pack(side=LEFT, padx=2, pady=2)

  def bEnter(self,event):
    self.bKey.config(text=self.bTextEnter)
    return
  
  def bLeave(self,event):
    self.bKey.config(text=self.bTextIdle)
    return
  
  def sUp(self,event):
    print self.bTextEnter
    #lOut.config(text='up')
    return
  
  def sDown(self,event):
    print self.bTextEnter
    #lOut.config(text='down')
    return




root = Tk()
b1 = bKey(root,idleText='1',enterText='a\nb')
b2 = bKey(root,idleText='2',enterText='c\nd')


# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = Message(master, text = whatever_you_do)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.bind('<Motion>',motion)
# msg.bind('<Button-4>',scrollUp)
# msg.bind('<Button-5>',scrollDown)
# msg.pack()
mainloop()
