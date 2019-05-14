
# function 1
def five_x_cubed_plus_1(x):
	return 5*x**3+1

# print(five_x_cubed_plus_1(2))
# print("==================================================")

# function 2
def pair_off(x):
	count = 0
	res = []
	for i in x:
		count = count + 1
		if count%2 == 1:
			temp = []
			temp.append(i)
		else:
			temp.append(i)
			res.append(temp)

	if len(temp)==1:
		res.append(temp)

	return res

# print(pair_off([2, 5, 1.5, 100, 3, 8, 7, 1, 1, 0, -2])) 
# print(pair_off([2, 5]))
# print(pair_off([1,2,3,4,5,6,7,8,9,10,11]))
# print("==================================================")

# function 3
def mystery_code(x):
	num = 0
	res = ""
	for i in range(len(x)):
		if x[i].isalpha():
			if x[i].isupper():
				num = ord(x[i].lower()) - ord("a")
				if num-7 < 0:
					num = abs(num-7)
					res += chr(122-num+1)
				else:
					res += chr(97 + num-7)
			else:	
				num = ord(x[i].upper()) - ord("A")
				if num-7 < 0:
					num = abs(num-7)
					res += chr(90-num+1)
				else:
					res += chr(65 +num-7)
		else:
			res += x[i]
	return res

# print(mystery_code("abc Iz th1s Secure? n0, no, 9!"))
# print(mystery_code("yoyo H0H1i2i3"))
# print(mystery_code("If you ArE 3 Years olD, What WILL YOU DO?"))
# print("==================================================")


def past_tense(x):
	length = 0
	res = []
	for i in x:

		if i=="have":
			res.append("had")
		elif i=="am" or i=="is":
			res.append("was")
		elif i=="are":
			res.append("were")
		elif i=="go":
			res.append("went")
		elif i=="eat":
			res.append("ate")
		elif i=="run":
			res.append("ran")
		else:
			temp = ""
			length = len(i)
			if i[length-1]=="y":
				if i[length-2]!="a" and i[length-2]!="e" and i[length-2]!="i" and i[length-2]!="o" and i[length-2]!="u":
					temp = i[0:length-2]+"ied"
					res.append(temp)
				else:
					temp = i + "ed"
					res.append(temp)
			elif i[length-1]=="e":
				temp = i + "d"
				res.append(temp)
			else:
				if i[length-2]=="a" or i[length-2]=="e" or i[length-2]=="i" or i[length-2]=="o" or i[length-2]=="u":
					if i[length-3]!="a" and i[length-3]!="e" and i[length-3]!="i" and i[length-3]!="o" and i[length-3]!="u":
						temp = i + i[length-1] + "ed"
						res.append(temp)
					else:
						temp = i + "ed"
						res.append(temp)
				else:
					temp = i + "ed"
					res.append(temp)

	return res

# print(past_tense(['program', 'debug', 'execute', 'crash', 'repeat', 'eat']))
# print(past_tense(['is']))
# print(past_tense(['are', 'go', 'run', 'hug', 'kiss']))

		
