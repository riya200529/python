num=int(input("enter num:"))
for i in range(1,num):
    for j in range(num,i,-1):
        print(j,end=" ")
    print()