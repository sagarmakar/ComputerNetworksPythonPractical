#definining

class LRC:
	
	def __init__(self, input1):
		self.data= input1



	def lrcodd(self):
		check = 0
		for i in range(len(self.data)):
			if self.data[i] == '1':
				check += 1
			else:
				continue

		if check%2 == 0:
			p = '1'
		else:
			p = '0'

		return p


	def lrceven(self):
		check = 0
		for i in range(len(self.data)):
			if self.data[i] == '1':
				check += 1
			else:
				continue

		if check%2 == 0:
			p = '0'

		else:
			p = '1'

		return p



class VRC:

	def __init__(self, input1):
		self.data= input1



	def vrcodd(self):
		vrc_value= ""

		for i in range(len(self.data[0])):
			count = 0
			for j in range(len(self.data)):
				if self.data[j][i]== '1':
					count += 1
				else:
					continue

			if count%2 == 0:
				p ='1'
			else:
				p = '0'
			
			vrc_value = vrc_value+ p		
			
		return vrc_value



	def vrceven(self):
		vrc_value= ""

		for i in range(len(self.data[0])):
			count = 0
			for j in range(len(self.data)):
				if self.data[j][i]== '1':
					count += 1
				else:
					continue

			if count%2 == 0:
				p ='0'
			else:
				p = '1'
				
			vrc_value = vrc_value+ p	
			
		return vrc_value







#Test

a= int(input("Choose: 1 for LRC and 2 for VRC: "))
	

if a ==1:

	b=int(input("Choose: 1 for odd parity and 2 for even: "))
	if b == 1:
		no_e = int(input("enter no of elements is your lrc, vrc data set: "))
		data1 =  ['']*no_e

		for i in range(no_e):
			c= str(input("insert your data for position " + str(i) + ": "))
			data1[i]= c
		
		print("LRC: -------------------")
		print("odd: ")
		for i in range(len(data1)):
			l = LRC(data1[i])
			print(data1[i] +" "+ l.lrcodd())
	if b == 2:
		no_e = int(input("enter no of elements is your lrc, vrc data set: "))
		data1 =  ['']*no_e

		for i in range(no_e):
			c= str(input("insert your data for position " + str(i) + ": "))
			data1[i]= c

		print("LRC: -------------------")
		print("even: ")
		for i in range(len(data1)):
			l = LRC(data1[i])
			print(data1[i] +" "+ l.lrceven())


if a== 2:
	b=int(input("Choose: 1 for odd parity and 2 for even: "))
	if b == 1:
		no_e = int(input("enter no of elements is your lrc, vrc data set: "))
		data1 =  ['']*no_e

		for i in range(no_e):
			c= str(input("insert your data for position " + str(i) + ": "))
			data1[i]= c

		print(" VRC: -------------------")
		v = VRC(data1)
		print("odd: ")
		for i in range(len(data1)):
			print(data1[i])
		print("--------")
		print(v.vrcodd())
	if b == 2:
		no_e = int(input("enter no of elements is your lrc, vrc data set: "))
		data1 =  ['']*no_e

		for i in range(no_e):
			c= str(input("insert your data for position " + str(i) + ": "))
			data1[i]= c

		print("VRC: -------------------")
		print("even: ")
		v = VRC(data1)
		for i in range(len(data1)):
			print(data1[i])
		print("--------")
		print(v.vrceven())