str = "It's thanskgiving day. It's my birthday too"
print str.find("day")
print str.replace("day" , " month")

===========================
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

========================
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
y = x[0] +" "+ x[-1]
print y

======================
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
b = x[:len(x)/2]
print b
c = x[len(x)/2:]
print c
d = [[b] + c]
print d
