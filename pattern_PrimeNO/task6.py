prime_no=0
not_prime=0
for num in range(1,101):
    temp=0
    for i in range(2,num):
        if num%i==0:
            temp=1
            not_prime += 1
            break
         
    if temp==0:
        prime_no+=1

print("count of prime number:",prime_no)
print("count of non-prime number:",not_prime)