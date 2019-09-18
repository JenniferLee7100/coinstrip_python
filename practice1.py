class Odd:
  def __init__(self, num):
    self.num = num

  def myfunc(self):
    i = 1 
    while i<5:
        self.num+=2
        print(self.num)
        i+=1
    

p1 = Odd(6)
p1.myfunc()