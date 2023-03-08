def start(obj):
    obj.speak()

class Animal:
    def speak(self):
        print('动物叫，但是不知道是什么动物')
class Dog(Animal):
    def speak(self):
        print('狗在叫')
class Cat(Animal):
    def speak(self):
        print('猫在叫')
class Car:
    def speak(self):
        print('车在叫')
start(Dog())
start(Cat())
start(Car())