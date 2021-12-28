def module_init(f):
  def pos_wrapper(x, y):
    def wrapper(tk):
      return f(tk, x, y)
    return wrapper
  return pos_wrapper
