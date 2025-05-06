import math

#time =o(log10(number))
n=142356789
num=n
count=0
while(num>0):
    num//=10
    count+=1
print(count)

#time=o(1)
num=n
count=0
print(int(math.log10(num))+1)