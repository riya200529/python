#write a program to square of number and store another list
list_1=[1,2,3]
ans=[]
#for i in list_1:
    #ans.append(i*i)
#print(ans)
ans=[i*i for i in list_1 if i%2==0]
print(ans)

#convert list elements into uppercase with list compresion