class Chain(object):
  def __init__(self,path=''):
    self._path = path
    
   def __getattr__(self,path):
    return Chain('%s/%s' % (self._path,path))
    
   __repr__ = __str__
