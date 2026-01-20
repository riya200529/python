#method-to access 
dict1={'india':'delhi','uk':'london','japan':'tokyo','france':'peris'}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print("iterating keys:")
for i in dict1.keys():
    print(i)

print("iterating value:\n\n")
for i in dict1.values():
    print(i)
    
print("iterating ltems:\n\n")
for i,j in dict1.items():
    print(i,j)