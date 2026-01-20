#ask user about the start and end increment value print accordingly:
start=int(input("enter start:"))
end=int(input("enter end:"))
increment=int(input("enter increment:"))
for i in range(start,end,increment):
    print(i)