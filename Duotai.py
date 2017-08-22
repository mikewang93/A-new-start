class Animal():
  def run(self):
    print "Animal is Running"
  
class Dog(Animal):
  def run(self):
    print "Run dog!"
    
class Cat(Animal):
  def run(self):
    print "Run cat!"
def run_twice(Animal):
  Animal.run()
  Animal.run()
a = Animal()
b = Dog()
c = Cat()

print "a is Animal?",isinctance(a,Animal)
print "b is Dog?",isinstance(b,Dog)
print "c is Cat?",isinstance(c,Cat)

run_twice(b)
