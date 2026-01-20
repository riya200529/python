#task:check list contains valid mobil num or not
#lst=['test1234','1234567890,123456789000,1234567,12345678910,'56565',7878twe]
#output: 1234567890, 12345678910
list=['test1234',1234567890,123456789000,1234567,12345678910,56565,'7878twe']
for i in list:
    if type(i)==int:
        length=len(str(i))
        if length==10:
            print(i)
    