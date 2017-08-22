class Screen(object):
  @property
  def width(self):
    return self._width
  @width.setter
  def width(self,value):
    self._width = value
    
  @property
  def height(self):
    return self._height
  @height.setter
  def height(self,num):
    self._height = num
    
  @property
  def resolution(self):
    return self._width * self._height
    
s = Screen()
s.width = 1080
s.height = 1920
print(s.resolution)
assert s.resolution == 2073600, '1024 * 768 = %d ?' % s.resolution
