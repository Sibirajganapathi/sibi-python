a={'id':1,'name':'sibi'}
print(a)
print(a['id'])
print(a['name'])
a['age']=21
print(a)
b={'course':'python'}
a.update(b)
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a.pop("id"))
print(a)