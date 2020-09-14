print("Manav Jain \n60004180050 \nA3")
d='1010110101100010101101100001'
ans = []
print("Hamming code = " + d)
for i in range(0,len(d)//7):
    data=list(d[7*i:7*(i+1)])
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

    if((error)==0):
        print('No Error found')

    elif((error)>=len(h_copy)):
        print('Multiple Error cannot be detected')

    else:
        print('Error found at',error,'bit')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'

        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            print('Corrected Hamming Code = ',end = "")
        h_copy.reverse()
        print(int(''.join(map(str, h_copy))))
    ans.append(int(''.join(map(str, h_copy))))

print(*ans)