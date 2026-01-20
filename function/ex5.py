#task:create fun check even or not isEven
#num%2=even 
def isEven(no):
    return no%2==0
     
num=int(input("enter number to check even or not:"))
ans=isEven(num)
print(f"answer is:{ans}")
