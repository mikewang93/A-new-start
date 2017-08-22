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
