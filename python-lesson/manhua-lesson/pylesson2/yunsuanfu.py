def f1():
  print("此处开始进入f1")
  return True

a = (1>0) or f1()
b = (1<0) or f1()
print(a)
print(b)
