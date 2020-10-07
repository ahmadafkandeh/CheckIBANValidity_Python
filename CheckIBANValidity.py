def CheckValidity(code):
	if len(code) != 26:
		return False
	print('input IBAN code: ', code)
	temp = code[4:]
	ch = str(int(ord(code[0])+2) - int(ord('A')+2) +10)
	temp += ch
	ch = str(int(ord(code[1])+2) - int(ord('A')+2) +10)
	temp += ch
	temp+= (code[2:4])
	print('calculated code:', temp)
	value = int(temp) % 97;
	if(value == 1 ):
		return True
	return False


if __name__ == "__main__":
	IBAN = input('Enter the IBAN Code: ')
	print('code valid: ',CheckValidity(IBAN))