for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()

for i in range(1,6,1):
    for j in range(0,6,1):
        print(i+j,end=" ")
    print()
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()
for i in range(65,91,1):
    for j in range(65,i+1,1):
        print(chr(j),end=" ")
    print()
for i in range(1,6,1):
    for j in range(6,1,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(" ",end=" ")
    for s in range(0,5,1):
        for j in range(0,s+1,1):
            print("*",end=" ")
    print()
for i in range(0,5,1):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(0,i+1,1):
        print("* ", end="")
    print() 
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print("* ",end=" ")
    print()