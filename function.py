#without argument&return value
def cube():
    a=int(input("enter a number"))
    print(a**5)
cube()
#without argument&with return value
def cube1():
    a=int(input("enter a number"))
    return a**5
print("cube1 of value",cube1())
#with argument&without return value
def add(a,b):
    print(a+b)
add(100+534)
#defult argument
def country(a="india"):
    print(a)
country()
country("pakisthan")
#keyword argument
def my(name,age):
    print(name," ",age)
my("sibi",21)
my(age=17,name="santhosh")