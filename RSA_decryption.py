def decryption(d,c,n) :
    c2=[]
    m=[]
    for i in c:
        x=((int(i)**int(d))%n)
        c2.append(x)
    #print(c2)
    for i in c2:
        m.append(chr(i))
    return m

def RSAdecryption():
    file=open("testfile.txt",'r')
    c1=file.read()  
    c=[]
    c=c1.split()
    file.close()
    #print(c)

    file=open("values.txt",'r')
    e1=file.readline()
    phi1=file.readline()
    n1=file.readline()
    file.close()

    e=int(e1)
    phi=int(phi1)
    n=int(n1)

    i=1
    for i in range(1,10000):
        x=e*i
        if((x%phi)==1):
            break
    d=int(i)

    m=[]
    m=decryption(d,c,n)
    final=''.join(map(str,m))
    output=str(final)
    ans='y'
    count=0

    while(ans=='y'):
        private_key=int(input("Enter Private Key:\t"))
        if(private_key!=d):
            print("Access Denied")
        else:
            file=open("decrypted data.txt",'w')
            file.write(output)
            file.close()
            print("data decrypted and stored in memory")
            break
        ans=input("try again?(y/n):\t")
        ans2=input("Want to know the private key?(y/n):\t")
        if(ans2=='y'):
            print(d)
        if(ans=='y'):
            count+=1
        if(count>2):
            print("Sorry, you exceeded the number of tries...")
            break

    input("Press Enter to exit")



RSAdecryption()
