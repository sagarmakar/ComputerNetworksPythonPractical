def checksumdecimal4bitsen(inp):
    i = 0
    sum = 0
    while i < len(inp):
        num = inp[i]
        sum = sum + num
        i += 1
    print("Sum in decimal is : ", sum)
    sum_to_bin = bin(sum).replace("0b", "").zfill(8)
    print("Coversion of the sum to binary : ", sum_to_bin)
    list_sum_to_bin = list(sum_to_bin)
    l1 = sum_to_bin[0:4]
    l2 = sum_to_bin[3:]
    sl1 = "0b" + str(l1)
    sl2 = "0b" + str(l2)
    print(sl1," ",sl2)

    add_bin = int(sl1, 2) + int(sl2, 2)
    wrappedsum = bin(add_bin)
    print("So the wrappedsum in binary is where 0b represents that its binary: ", wrappedsum)
    print("So the wrappedsum in decimal is: ", int(wrappedsum, 2))
    check = list((wrappedsum.replace('0b', '')).zfill(4))
    checksum = []
    for i in check:
        if i == '0':
            checksum.append("1")
        else:
            checksum.append("0")
    checks = ''.join(checksum)
    checksums = '0b' + checks
    print("So the value of the checksum in binary is: ", checksums)
    print("So the value of the checksum is ", int(checksums, 2))


def checksumdecimal4bitrec(inp):
    i = 0
    sum = 0
    while i < len(inp):
        num = inp[i]
        sum = sum + num
        i += 1
    print("Sum in decimal is : ", sum)
    sum_to_bin = bin(sum).replace("0b", "").zfill(8)
    print("Coversion of the sum to binary : ", sum_to_bin)
    list_sum_to_bin = list(sum_to_bin)
    l1 = sum_to_bin[0:4]
    l2 = sum_to_bin[3:]
    sl1 = "0b" + str(l1)
    sl2 = "0b" + str(l2)
    print(sl1," ",sl2)

    add_bin = int(sl1, 2) + int(sl2, 2)
    wrappedsum = bin(add_bin)
    print("So the wrappedsum in binary is where 0b represents that its binary: ", wrappedsum)
    print("So the wrappedsum in decimal is: ", int(wrappedsum, 2))
    check = list((wrappedsum.replace('0b', '')).zfill(4))
    checksum = []

    for i in check:
        if i == '0':
            checksum.append("1")
        else:
            checksum.append("0")
    checks = ''.join(checksum)
    checksums = '0b' + checks
    print("So the value of the checksum in binary is: ", checksums)
    print("So the value of the checksum is in decimal : ", int(checksums, 2))
    if int(checksums, 2) == 0000:
        print("Correct Data received")
        print("Data received is: ", data)
    else:
        print("Incorrect data received")



def checksumdecimal8bitsen(inp):
    i = 0
    sum = 0
    while i < len(inp):
        num = inp[i]
        sum = sum + num
        i += 1
    print("Sum in decimal is : ", sum)
    sum_to_bin = bin(sum).replace("0b", "").zfill(16)
    print("Coversion of the sum to binary : ", sum_to_bin)
    list_sum_to_bin = list(sum_to_bin)
    l1 = sum_to_bin[0:8]
    l2 = sum_to_bin[7:]
    sl1 = "0b" + str(l1)
    sl2 = "0b" + str(l2)
    print(sl1," ",sl2)

    add_bin = int(sl1, 2) + int(sl2, 2)
    wrappedsum = bin(add_bin)
    print("So the wrappedsum in binary is where 0b represents that its binary: ", wrappedsum)
    print("So the wrappedsum in decimal is: ", int(wrappedsum, 2))
    check = list((wrappedsum.replace('0b', '')).zfill(8))
    checksum = []
    for i in check:
        if i == '0':
            checksum.append("1")
        else:
            checksum.append("0")
    checks = ''.join(checksum)
    checksums = '0b' + checks
    print("So the value of the checksum in binary is: ", checksums)
    print("So the value of the checksum is ", int(checksums, 2))




def checksumdecimal8bitrec(inp):
    i = 0
    sum = 0
    while i < len(inp):
        num = inp[i]
        sum = sum + num
        i += 1
    print("Sum in decimal is : ", sum)
    sum_to_bin = bin(sum).replace("0b", "").zfill(16)
    print("Coversion of the sum to binary : ", sum_to_bin)
    list_sum_to_bin = list(sum_to_bin)
    l1 = sum_to_bin[0:8]
    l2 = sum_to_bin[7:]
    sl1 = "0b" + str(l1)
    sl2 = "0b" + str(l2)
    print(sl1," ",sl2)

    add_bin = int(sl1, 2) + int(sl2, 2)
    wrappedsum = bin(add_bin)
    print("So the wrappedsum in binary is where 0b represents that its binary: ", wrappedsum)
    print("So the wrappedsum in decimal is: ", int(wrappedsum, 2))
    check = list((wrappedsum.replace('0b', '')).zfill(8))
    checksum = []

    for i in check:
        if i == '0':
            checksum.append("1")
        else:
            checksum.append("0")
    checks = ''.join(checksum)
    checksums = '0b' + checks
    print("So the value of the checksum in binary is: ", checksums)
    print("So the value of the checksum is in decimal : ", int(checksums, 2))
    if int(checksums, 2) == 0000:
        print("Correct Data received")
        print("Data received is: ", data)
    else:
        print("Incorrect data received")




def checksum2sen(sender):
    lst = []
    total = 0
    for c in sender:
        lst.append(ord(c))
    print(lst)

    hexlst = []
    for s in lst:
        hexlst.append(hex(s))
    print(hexlst)

    hexl=[]

    for a in hexlst:
        hexl.append(a.split('x')[1])
    print(hexl)

    newl = []
    i = 0
    while i < len(hexl):
        newl.append(hexl[i] + hexl[i + 1])
        i = i + 2
    print("compoments to be added of headecimal: ", newl)

    i = 0
    while i < len(newl):
        total += int(newl[i], 16)
        i = i + 1

    print("Total sum :", hex(total))

    s = hex(total).split('x')[1]
    s1 = s[1:]
    s2 = s[0]
    wrapsum = int(s1, 16) + int(s2, 16)
    w = hex(wrapsum)
    print("Wrapsum is: ", hex(wrapsum))
    wsum = w.split('x')[1]
    print(wsum)
    csum = bin(int(wsum, 16))
    print(csum)
    csum_l = list(csum)
    j = 0
    checkl = []
    for j in csum:
        if j == '1':
            checkl.append('0')
        else:
            checkl.append('1')
    checks = ''.join(checkl)
    print("So the checksum is ", hex(int(checks[2:], 2)))

def checksum2rec(inp):
    m = 0
    sum=0
    print("Hexadecimal list is ", inp)
    while m < len(inp):
        sum += int(inp[m], 16)
        m = m + 1
    print("The total sum is: ", hex(sum))
    wr = hex(sum).split('x')[1]
    wr1 = wr[1:]
    wr2 = wr[0]
    r_wrapsum = int(wr1, 16) + int(wr2, 16)
    r_w = hex(r_wrapsum)
    print("Wrapsum is: ", hex(r_wrapsum))
    r_wsum = r_w.split('x')[1]
    print(r_wsum)
    r_csum = bin(int(r_wsum, 16))
    print(r_csum)
    r_csum_l = list(r_csum)
    n = 0
    r_checkl = []
    for n in r_csum:
        if n == '1':
            r_checkl.append('0')
        else:
            r_checkl.append('1')
    r_checks = ''.join(r_checkl)
    r_hex = hex(int(r_checks[2:], 2))
    r_hex1 = (r_hex.split('x')[1]).zfill(4)
    print("So the checksum is ", r_hex1)

    if (r_hex1 == '0000'):
        print("Correct data received")
    else:
        print("Incorrect data is being received")








a= int(input("enter 1 for decimal and 2 for strings: "))

if a==1:
	bit= int(input("enter 1 for 4bit and 2 for 8bit checksums: "))

	if bit==1:

		b= int(input("enter 1 for sender and 2 for reciever: "))

		if b==1:
			print("                Senders Side                 ")
			print("---------------------------------------------\n")
			inp1=[]
			c=int(input("number of elements: "))
			for i in range(c):
				d= int(input("enter the number for "+ str(i)+ " position: "))
				inp1.append(d)

			checksumdecimal8bitsen(inp1)

		if b==2:
			print("                Recievers Side                 ")
			print("---------------------------------------------\n")
			inp1=[]
			c=int(input("number of elements: "))
			for i in range(c):
				d= int(input("enter the number for "+ str(i)+ " position: "))
				inp1.append(d)

			checksumdecimal8bitrec(inp1)
		else:
			print("enter valid option")


	if bit==2: 


		b= int(input("enter 1 for sender and 2 for reciever: "))

		if b==1:
			print("                Senders Side                 ")
			print("---------------------------------------------\n")
			inp1=[]
			c=int(input("number of elements: "))
			for i in range(c):
				d= int(input("enter the number for "+ str(i)+ " position: "))
				inp1.append(d)

			checksumdecimal8bitsen(inp1)

		if b==2:
			print("                Recievers Side                 ")
			print("---------------------------------------------\n")
			inp1=[]
			c=int(input("number of elements: "))
			for i in range(c):
				d= int(input("enter the number for "+ str(i)+ " position: "))
				inp1.append(d)

			checksumdecimal4bitrec(inp1)

		else:
			print("enter valid option")


if a==2:

	b= int(input(" enter 1 for sender and 2 for reciever: "))

	if b==1:
		print("")
		print("                Senders Side                 ")
		print("---------------------------------------------\n")
		sender = input("Enter the senders message: ")
		if len(sender) % 2 == 1:
			sender = '0' + sender
		else:
			sender = sender
		checksum2sen(sender)

	if b==2:
		print("                Recievers Side                 ")
		print("---------------------------------------------\n")
		inpt=int(input('Enter the total times you want to input: '))
		rlist = []
		input_string = input("Enter a list elements separated by space in receiver side: ")
		userList = input_string.split()
		checksum2rec(userList)

	else:
		print("enter valid option")

else:
	print("enter valid option")