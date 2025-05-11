import math
n=93
cnt=0
for i in range(1,int(math.sqrt(n)+1)):
    if(n%i==0):
        cnt+=1
    if(cnt>2):
        
        break
if(cnt>2):
    print("Not prime")
else:
    print("prime")