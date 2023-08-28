for i in range(1,9,2):
    for j in range(int((7-i)/2)): print(" ",end="")
    for j in range(i): print(i,end="")
    for j in range(int((7-i)/2)): print(" ",end="")
    print()
