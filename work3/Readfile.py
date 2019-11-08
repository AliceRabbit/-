# -*- coding: UTF-8 -*-
from operator import is_

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])
 
    return ''.join([str(x) for x in mid[::-1]])

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

def is_same(list):
    for i in range(len(list)-1):
        for j in [i+1,len(list)-1]:
            if(list[i]==list[j]):
                print i,j
 
def print_list(string,list):   
    print string,'***************************************************************************'
    for i in range(len(list)):
        if(i<=9):print  str(i),'',list[i],str(i)
        else:print str(i),list[i],str(i)
        
def decryped(num,string,string2): 
    c,a,count=[],'',0  
    for i in range(len(string)):
        a+=string[i]
        count+=1
        if(count%2==0):
            count=0
            c.append(a)
            a=''
    for i in c:
        a+=chr(int(i.upper(), 16))    
    print 'Part',num,'---->',a
 
def fun(x,n,N): 
    '''快速模取幂算法'''
    res=1  
    while n>0:  
        if(n & 1): 
            res=(res*x)%N 
        x=(x*x)%N 
        n >>= 1 
    return res 
 
def match(allkinds,n,e,c,num_of_Frame):
    a=''
    for i in range(len(allkinds)):
       a+=dec2hex(ord(allkinds[i]))
    #print 'a',a
    n2=int(hex2dec(n))
    #print 'n2',n2,type(n2)
    a2=int(hex2dec('0x9876543210ABCDEF'+dec2hex(num_of_Frame).zfill(8)+'0'*88+a))
    #print 'a2',Base.dec2hex(str(a2)),Base.dec2hex(num_of_Frame).zfill(8)
    e2=int(hex2dec(e))
    #print 'e2',e2
    #print 'c',c
    un_c=fun(a2,e2,n2)
    un_c2=dec2hex(str(un_c))
    #print 'un_c2',un_c2
    if(un_c2==c):return 1
    else:return 0
    
m,N,e,c=[],[],[],[]
filename=['Frame'+str(i) for i in range(21)]
for i in range(21):
    fd = open(filename[i],'r')
    m.append(fd.read())
    fd.close()
for frame in m:
    N.append(frame[0:256])
    e.append(frame[256:512])
    c.append(frame[512:768])
    
# print_list('N=',N)
# print_list('e=',e)
# print_list('c=',c)
 
 
decryped(0,'4D79207365637265','From Frame 0 and 4')
decryped(1,'7420697320612066','From Frame 3,8,12,16 and 20')
decryped(5,'696E737465696E2E','From Frame 19')
decryped(6,'2054686174206973','From Frame 2')
decryped(7,'20224C6F67696320','From Frame 6')
decryped(8,'77696C6C20676574','From Frame 10')
decryped(9,'20796F752066726F','From Frame 14')
decryped(10,'6D204120746F2042','From Frame 18')
decryped(11,'2E20496D6167696E','From Frame 1')
 
 
print match('m A to B', N[18], e[18], c[18], 10)
 
def final_match(mingwen):
    for i in range(20):
        for j in range(20):
            if(match(mingwen, N[i], e[i], c[i], j)):print 'seccessful','Result is right!!','Frame',i,'<======>','Part',j
 
'''
以下都是我们的猜测字符串，然后进行匹配
'''
mingwen2=['ll take ','you ever','ywhere. ']
for i in mingwen2:
    final_match(i)