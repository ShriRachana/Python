x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
b = x[:len(x)/2]
print b
c = x[len(x)/2:]
print c
d = [[b] + c]
print d
