class Animal:
    def __init__(self,name):
        self.name =name

    def show_info(self):
        return '动物的名字：{0}'.format(self.name)

    def move(self):
        print('动一动...')

class Cat(Animal):
    def __init__(self, name,age):
        super().__init__(name) #调用父类的构造方法（自动补全！）
        self.age=age #实际变量age
    def ages(self):
        return '动物的年龄：{0}'.format(self.age)

cat =Cat('Tom',2)
cat.move()
print(cat.show_info())
print(cat.ages())