arr=[1,0,0,10,10,4,2,7,3,5,4,10,0,9]
# arr=list(set(arr))
# arr.sort()
# print(arr[1]," and ",arr[-2])

small,second_small=float('inf'),float('inf')
large,second_large=float('-inf'),float('-inf')
for i in arr:
    if i<small:
        second_small=small
        small=i
    elif i<second_small and i!=small:
        second_small=i
    if i>large:
        second_large=large
        large=i
    elif i>second_large and i!=large:
        second_large=i
print(second_small,second_large)