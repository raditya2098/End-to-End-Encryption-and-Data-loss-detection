import SHA256
import random

def check_prime(n):
    flag=0
    n1=int((n/2)-0.5)
    for i in range(2,n1):
        if n%i==0:
            flag=1
            break
        else:
            flag=0

    return(flag)

def check_mod(a,b,c):
    x=a*b
    if x%c==1:
        return 0
    else:
        return 1

def DSAsignature():
    p=random.randint(100,1000)  
    while(check_prime(p)!=0):
        p=random.randint(100,1000)
    p1=int(p-1)
    q=2

    for i in range(int(p1/2),2,-1):
        if p1%i==0:
            if check_prime(i)==0:
                q=i
                break

    h=2
    p1q=p1/q
    g=int((pow(h,p1q))%p)   

    x=random.randint(1,q)
    y=int((pow(g,x))%p)
    k=random.randint(1,q)
    r=0
    s=0
    z=0
    for i in range(1,1000):
        if check_mod(k,i,q)==0:
            z=i
            break
        
    while(r==0 or s==0):
        r1=(pow(g,k))%p
        r2=r1%q
        r=int(r2)
        if r==0:
            k=random.randint(1,q)
        msg=SHA256.msg
        hash_val=SHA256.hash_value

        s1=int(hash_val,16)+(x*r)
        s2=s1*z
        s3=s2%q
        s=int(s3)
        if s==0:
            k=random.randint(1,q)

    print('p ',p,'\nq ',q,'\ng ',g,'\nx',x,'\ny',y,'\nk',k,'\nr',r,'\ns',s)

    msg_l=[]
    for i in range(len(msg)):
        msg_l.append(ord(msg[i]))

    msg_final=' '.join(map(str,msg_l))
    length=len(msg_l)
    file=open('signature_values.txt','w')
    file.write(str(length))
    file.write(' ')
    file.write(msg_final)
    file.write(' ')
    file.write(str(r))
    file.write(' ')
    file.write(str(s))
    file.write(' ')
    file.write(str(p))
    file.write(' ')
    file.write(str(q))
    file.write(' ')
    file.write(str(g))
    file.write(' ')
    file.write(str(y))
    file.close()

DSAsignature()
