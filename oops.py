#basic program
class employee:
    def fun1(self):
        print("hello")
    def fun2(self):
        print("welcome")
e1=employee()
e1.fun2()
#instancemethod
class employee:
    def detail(self,id,name):
        self.i=id
        self.n=name
        print(id)
        print(name)
    def show(self):
        print(self.i)
e1=employee()
e1.detail(12,"sibi")
e1.show()
#staticemethod
class person:
    @staticmethod
    def fun1(a,b):
        c=a+b
        print(c)
p=person()
p.fun1(456,678)
#class method
class employee:
    course ="python"
    def fun1(self,name,age):
        self.n=name
        self.a=age
    def fun2(self):
        print("student name",self.n)
        print("student age",self.a)
        print("student course",employee.course)
    @classmethod
    def detail(cls):
        cls.course="java"
e=employee()
e.fun1("sibi",23)
employee.detail()
e.fun2()