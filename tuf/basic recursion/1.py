
def recursion(cnt):

    print(cnt)
    cnt+=1
    if(cnt<3):
        recursion(cnt)
cnt=0
recursion(cnt)