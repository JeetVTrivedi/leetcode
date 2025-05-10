n=371
num=n
cnt=0
digit=0
sum=0
while(num>0):
    cnt+=1
    num=num//10
num=n
while(num>0):
    digit=num%10
    sum+=digit**cnt
    num=num//10
if(n==sum):
    print("Armstrong number")
else:
    print("not armstrong")