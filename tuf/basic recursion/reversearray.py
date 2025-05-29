arr=[1,2,3]
for i in range(((len(arr)-1)//2)+1):
    arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
print(arr)

