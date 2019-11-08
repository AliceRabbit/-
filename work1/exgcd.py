A=[0,1]
N=[1,0]
A.append(int(input('Please input a:')))
N.append(int(input('Please input n:')))
def Extended_Euclid(a,n):
    if a[2]==0:
        print('无逆元,gcd(%d,%d)= %d'%(a[2],n[2]))
    elif a[2]==1:
        print('gcd(a,n)=%d\na的逆元: %d'%(a[2],a[1]))
    else:
        Q=n[2]//a[2]
        t1,t2,t3=[(n[0]-Q*a[0]),(n[1]-Q*a[1]),(n[2]-Q*a[2])]
        Extended_Euclid([t1,t2,t3],[a[0],a[1],a[2]])
 
solution=Extended_Euclid(A,N)
 