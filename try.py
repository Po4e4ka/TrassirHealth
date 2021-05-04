dict1 = {'1':{'5':3}, '2':2}
for i in dict1:
    del dict1["1"]

print(dict1.items())