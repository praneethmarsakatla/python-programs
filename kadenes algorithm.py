def Kadane(a):
    max_current=max_global=a[0]
    for i in range(1,len(a)):
        max_current=max(a[i],max_current+a[i])
        max_global=max(max_global,max_current)
    return max_global
a=[2,3,-10,4,-2,5,-1]
print(Kadane(a))
