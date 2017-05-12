sI = [1,43,6,65]
type(sI)
if (type(sI) == int and sI>=100):
    print "That is a big number"
elif (type(sI) == int and sI<=100):
    print "Not a big number"
elif (type(sI) == str and len(sI)>50):
    print "That is a big sentence"
elif (type(sI) == str and len(sI)<50):
    print "That is a okay sentence"
elif(type(sI) == list and len(sI)>=10):
     print "That is a big list"
elif (type(sI) == list and len(sI)<50):
    print "That is a okay list"
else:
    print"Probably missed it by the length"
