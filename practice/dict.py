thisdict={'a':1,'b':1,'c':2}

thisdict.update({'d':3})
a='d'
thisdict.pop(a)
for i,j in thisdict.items():
    print(i,j)