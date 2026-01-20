#function declaration fun with no perameter no return
def greet():
    print("have good day")
#with single perameter
def greet1(name):
    print("have a good day",name)

#fun with 2 perameter and return value#add 2 val & return sum
def add(no1,no2):
    return no1+no2
greet()
greet1("ami")
greet1("riya")
greet1("piya")
ans=add(20,70)
print(f"sum is:{ans}")