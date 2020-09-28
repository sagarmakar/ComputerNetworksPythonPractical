def StringToBinary(S=""):
    return[bin(ord(x))[2:].zfill(8) for x in S]
S=input("Enter your string: ")
B=StringToBinary(S)
uinput=int(input("Press 1 for bit oriented and 2 for byte orinted: "))
if uinput==1:
    print("\n \n Bit Orinted")
    print(" --------------------------------- \n\n")
    print("\nBinary Conversion of input: ",B)
    count=0
    i=0
    while(i<len(B)):
        if(B[i]=='1'):
            count+=1
        else:
            count=0
        if (count==6):
            B.insert(i,'0')
            ary=i
            count=0
        i+=1
    start_frame=end_frame='01111110'
    x=''
    x=''.join(B)
    Z=start_frame+x+end_frame
    print("\nSender side data:",Z)

    list_Z=list(Z)
    length=len(list_Z)
    odata=list_Z[8:length-8]
    rdata=''.join(odata)
    print("\nReceiver Side Data in binary",rdata)
    print("\nDecoded Received Data : ",S)
elif uinput==2:
    print("\n \n Byte Orinted")
    print(" --------------------------------- \n\n")
    flag='@'
    escape='$'
    blist=list(S)
    i=0
    length =len(blist)
    for i in range(length):
        if blist[i]=='@':
            blist.insert(i,'$')
            arr=i
            break
    x=''.join(blist)
    Z=flag+x+flag
    print("Sender Side (Byte Stuffing) -",Z)
    ustf=list(Z)
    del ustf[0]
    del ustf[-1]
    del ustf[arr]
    string=''.join(ustf)
    print("Receiver Side :",string)
else:
    print("Enter a valid number pressed")