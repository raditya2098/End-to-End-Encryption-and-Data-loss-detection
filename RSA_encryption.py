import random


def checkprime(p):
    for i in range(2,p-1):
        if(p%i==0):
            flag=0
            break
        else:
            flag=1
    return flag


def checkgcd(a,b):
    c=min(a,b)
    for i in range(2,c+1):
        if((a%i==0) and (b%i==0)):
            flag=0
            break
        else:
            flag=1
    return flag


def encryp(e,n):
    path=input("Enter the path of the text file to be encrypted (use '/' slash instead of '\'):\t")
    file=open(path,'r')
    l=file.read()
    file.close()
    m=[]
    for ch in l:
        m.append(ord(ch))
    #print(m)
    i=0
    c=[]
    for i in m:
        x=((i**e)%n)
        c.append(x)
    return c

def RSAencryption():
    p=(random.randint(1,100))
    while(checkprime(p)!=1):
        p=(random.randint(1,100))
    z=8
    q=p+z
    while(checkprime(q)!=1):
        q=p+z
        z-=2

    n=p*q
    phi=(p-1)*(q-1)
    e=3
    while(checkgcd(e,phi)!=1):
        e+=1
    #print('1')

    c=[]
    #print('p=',p,'\nq=',q,'\ne=',e,'\nphi=',phi,'\nn=',n)

    c1=encryp(e,n)
    c=[]
    ch='a'
    for ch in c1:
        c.append(int(ch))
    #print(c)
    str_c=" ".join(map(str,c))  
    #print(str_c)
    file=open("testfile.txt",'w')
    file.write(str_c)
    file.close()    
    print("Message has been encrypted")
    print("If you want to check the encrypted data, open testfile.txt on your system")

    file=open("values.txt",'w')
    file.write(str(e))
    file.write('\n')
    file.write(str(phi))
    file.write('\n')
    file.write(str(n))
    file.close()


    input("Press Enter to exit")

RSAencryption()



