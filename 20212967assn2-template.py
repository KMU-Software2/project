def recbinsearch(L,l,u,target):
    midnum = (l + u) // 2
    if L[midnum] == target:
        return midnum
    elif L[midnum] > target:
        return recbinsearch(L,l,midnum-1,target)
    else:
        return recbinsearch(L,midnum+1,u,target)
