def caesarCipherEncryptor(string, key):
    # Write your code here.
    def newchar(oldchar,key):
		newcode=ord(oldchar)+key
		return chr(newcode) if newcode<=122 else chr(96 + newcode%122)
	outstring=[]
	key=key%26
	for each in string:
		outstring.append(newchar(each,key))
	return ''.join(outstring)
