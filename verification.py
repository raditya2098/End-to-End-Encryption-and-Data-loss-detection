import SHA256_copy

def check_mod(a,b,c):
    x=a*b
    if x%c==1:
        return 0
    else:
        return 1

def DSAverification():
    file=open('signature_values.txt','r')
    inp_file=file.read()
    file.close()

    contents=[] 
    for i in range(len(inp_file)):
        contents.append(inp_file[i])
    len_1=[]
    cnt=0
    for i in range(len(contents)):
        if contents[i]!=' ':
            len_1.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break

    len_str=''.join(map(str,len_1))
    length=int(len_str)
    #print(length)
    white_count=0
    msg_ascii=[]
    while(white_count!=length):
        temp_l=[]
        for i in range(cnt,len(contents)):
            if contents[i]!=' ':
                temp_l.append(contents[i])
                cnt+=1
            else:
                cnt+=1
                break
        temp=''.join(map(str,temp_l))
        msg_ascii.append(temp)
        white_count+=1

    #print('            ',msg_ascii)
    msg_l=[]
    for i in range(len(msg_ascii)):
        msg_l.append(chr(int(msg_ascii[i])))

    msg_ver=''.join(map(str,msg_l))
    s_l=[]
    r_l=[]
    p_l=[]
    q_l=[]
    y_l=[]
    g_l=[]
    for i in range(cnt,len(contents)):
        if contents[i]!=' ':
            r_l.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break

    for i in range(cnt,len(contents)):
        if contents[i]!=' ':
            s_l.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break

    for i in range(cnt,len(contents)):
        if contents[i]!=' ':
            p_l.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break

    for i in range(cnt,len(contents)):
        if contents[i]!=' ':
            q_l.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break

    for i in range(cnt,len(contents)):
        if contents[i]!=' ':
            g_l.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break

    for i in range(cnt,len(contents)):
        if contents[i]!=' ':
            y_l.append(contents[i])
            cnt+=1
        else:
            cnt+=1
            break
    
    s_ver=''.join(map(str,s_l))
    r_ver=''.join(map(str,r_l))
    p_ver=''.join(map(str,p_l))
    q_ver=''.join(map(str,q_l))
    g_ver=''.join(map(str,g_l))
    g=int(g_ver)
    y_ver=''.join(map(str,y_l))
    #print(msg_ver)
    #print(s_ver)
    #print(r_ver)
    s_rec=int(s_ver)
    r_rec=int(r_ver)
    p=int(p_ver)
    q=int(q_ver)
    y_rec=int(y_ver)
    #print(contents)
    h_rec=SHA256_copy.hash_value
    #print(h_rec)
    w=0
    for i in range(0,10000):
        if check_mod(s_rec,i,q)==0:
            w=i
            break
        else:
            w=1

    
    u1_a=(int(str(h_rec),16))*w
    u1=(u1_a)%q

    u2_a=(r_rec)*w
    u2=(u2_a)%q
    #print(y_rec)
    #print(u1,u2)
    ans='y'
    while(ans=='y'):
        y_inp=input("Enter public key:  ")
        if (y_inp!=str(y_rec)):
            ans=input("Wrong key!!!!!!\t Try again?(y/n)")
        else:
            v1=(int(g)**u1)*(int(y_inp)**u2)
            v=(v1%p)%q
            #print(round(v))
            print('message:\n',msg_ver)
            break


DSAverification()
