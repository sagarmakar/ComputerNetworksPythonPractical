class CRC:
	
	def __init__(self):
		self.cdw = ''

	def xor(self,a,b):
		result = []
		for i in range(1,len(b)):
			if a[i] == b[i]:
				result.append('0')
			else:
				result.append('1')


		return  ''.join(result)



	def crc(self,message, key):
		pick = len(key)

		tmp = message[:pick]

		while pick < len(message):
			if tmp[0] == '1':
				tmp = self.xor(key,tmp)+message[pick]
			else:
				tmp = self.xor('0'*pick,tmp) + message[pick]

			pick+=1

		if tmp[0] == "1":
			tmp = self.xor(key,tmp)
		else:
			tmp = self.xor('0'*pick,tmp)

		checkword = tmp
		return checkword

	def encodedData(self,data,key):
		l_key = len(key)
		append_data = data + '0'*(l_key-1)
		remainder = self.crc(append_data,key)
		codeword = data+remainder
		self.cdw += codeword
		print("Remainder: " ,remainder)
		print("Data: " ,codeword)

	def reciverSide(self,key,data):
		r = self.crc(data,key)
		size = len(key)
		print(r)


print("------------------- CRC -------------------")
c = CRC()
print(" ")
data = str(input("data for CRC: "))
key = str(input("key for CRC: "))
print(" ")
print('------------ At sender Side ------------ ')
c.encodedData(data,key)
print(" ")
print("------------ At reciver Side ------------")
print("checkword of codeword and key:", end= " ")
c.reciverSide(c.cdw, key)
print(" ")
print("Code Word:", end= " ")
print(c.cdw)