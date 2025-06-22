inp=[5,1,1,2,3,4,4,4]
cnt={}
for i in inp:
    if i  in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
print(cnt)