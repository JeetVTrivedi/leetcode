s="abcdaba"
inp=['a','b','c','z','e']
count=[0]*26
for chr in s:
    index=ord(chr)-ord('a')
    count[index]+=1
for chr in inp:
    print(chr," ",count[ord(chr)-ord('a')])