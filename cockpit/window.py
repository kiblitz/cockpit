import tkinter

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
    self.components = []

  def display(self):
    dimensions = (self.width*self.block_size, self.height*self.block_size)
    root = tkinter.Tk()
    root.title(self.title)
    self.preprocessing(root)
    root.geometry("%dx%d" % dimensions)
    root.resizable(False, False)

    for component_init in self.components:
      components_init(root)

    root.mainloop()

  def add_component(component, x, y):
    abs_x, abs_y = x * self.block_size, y * self.block_size
    self.components.append(component.init(abs_x, abs_y))

def new(**kwargs):
  return _Window(**kwargs)
