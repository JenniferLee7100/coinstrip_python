print("Hello World")
if True:
   print("True")
else:
   print("False")

counter = 12320
miles = 29.42
name = "Peter"

print(counter)
print(miles)
print(name)

a = b = c = 12
d,e,r = 1,2,"jeo"

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
