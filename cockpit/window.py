import tkinter
import threading

FLOATING = lambda root: root.attributes('-type', 'dialog')

class _Window:
  def __init__(self, 
               block_size=100, 
               width=8, height=6, 
               title='cockpit',
               preprocessing=lambda _: None):
    self.block_size = block_size
    self.width = width
    self.height = height
    self.title = title
    self.preprocessing = preprocessing

  def display(self):
    def tk_init():
      dimensions = (self.width*self.block_size, self.height*self.block_size)
      root = tkinter.Tk()
      root.title(self.title)
      self.preprocessing(root)
      root.geometry("%dx%d" % dimensions)
      root.mainloop()
    threading.Thread(target=tk_init).start()

def new(**kwargs):
  return _Window(**kwargs)