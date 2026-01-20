age=int(input("enter age"))
if age>=0 and age<=2:
    print("infant")
elif age>=3 and age<=18:
    print("minor")
elif age>=19 and age<=50:
    print("major")
elif age>=51 and age<=70:
    print("supersenior")
elif age>=71 and age<=90:
    print("supersenior")

else:
    print("invalid")