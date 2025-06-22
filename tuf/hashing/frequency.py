inp=[1,1,1,2,3,4,5,2,3,4]
cnt={}

for i in inp:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
maxx=max(cnt,key=cnt.get)
minn=min(cnt,key=cnt.get)
print(maxx, minn)