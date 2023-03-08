class Dog:
    def __init__(self,name,age):
        self.name = name #创建并初始化实际变量name
        self.__age = age
    def run(self):
        print("{}在跑...".format(self.name))
    def speak(self,sound):
        print('{}在叫，"{}"!'.format(self.name,sound))
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age

dog =Dog('球球',2)
print('我们家的狗名字叫{0}，已经{1}岁了.'.format(dog.name,dog.age))
dog.run()
dog.speak("汪，汪，汪")