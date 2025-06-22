def calc(arr,k):
    maxx=0
    summ=0
    n=0
    l=0
    freq={}
    for r in range(len(arr)):
        summ+=arr[r]
        n+=freq.get(arr[r],0)==0
        freq[arr[r]]=freq.get(arr[r],0)+1
        while n>k:
            n-=freq[arr[l]]==1
            freq[arr[l]]-=1
            summ-=arr[l]
            l+=1
        maxx=max(maxx,summ)
    while l<r:
        freq[arr[l]]-=1
        summ-=arr[l]
        maxx=max(maxx,summ)
        l+=1
    return maxx
print(calc([1,2,2,3,2,3,5,1,2,1,1],2))
print(calc([-1,-2,-3],1))
print(calc([-1,1,3,2,-1],5))