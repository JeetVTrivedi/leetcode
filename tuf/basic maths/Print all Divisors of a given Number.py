div=[]
n=36
for i in range(1,(n//2)+1):
    if(n%i==0):
        div.append(i)
div.append(n)
print(div)