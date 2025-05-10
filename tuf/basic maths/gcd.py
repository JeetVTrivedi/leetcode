n,m=20,45
small=min(n,m)
gcd=0
if(max(n,m)%min(n,m)==0):
    print(min(n,m))
else:
    
    for i in range(1,(small//2)+1):
        if(n%i==0 and m%i==0):
            gcd=i
    print(gcd)
    
#USING EUCLIDIEAN ALGORITHM
a,b=20,40
while(a>0 and b>0):
    if(a>b):
        a=a%b
    else:
        b=b%a
if(a==0):
    print(b)
else:
    print(a)