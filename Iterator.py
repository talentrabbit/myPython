#Iterator examples
d={'key1':1,'key2':2, 'key3':3}
for val in d.values():
    print(val)

l = list(range(1,10))
print(l)

var = [i *i for i in l]
print (var)