#if enter num is even then print table
num=int(input("enter num:"))
i=1
if num%2==0:
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
else:
    print("only even num")
