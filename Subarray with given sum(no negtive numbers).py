def SubArraySum(a,s,n):
    st=a[0]
    j=0
    i=1
    while i<=n:
        while st>s and j<i-1:
            st=st-a[j]
            j=j+1
        if st==s:
            print('subarray from ',j,'to ',i-1)
            return 1
        if i<n:
            st=st+a[i]
        i+=1
    cout<<'not found'
    


if __name__=="__main__":
    n=int(input())
    s=int(input())
    a= [ int(x) for x in input().split()]
    SubArraySum(a,s,n)


