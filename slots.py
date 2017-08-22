class Teacher(object):
  __slots__ = ('name','age')
  pass
  
class Student(Teacher):
  pass
  
t = Teacher()
t.name = 'Leo'
t.age = 24
print t.name
print t.age

try:
  t.score = 99
except AttributeError as e:
  print 'Attribute is',e
  
 s = Student()
 s.score = 100
 print 's.score =',s.score
