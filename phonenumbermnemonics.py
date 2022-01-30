def phoneNumberMnemonics(phoneNumber):
    key_mapping={'0':['0'],'1':['1'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
	if(phoneNumber=='1' or phoneNumber=='0'):
		return [str(phoneNumber)]
	def util(i,phoneNumber,new,Mset):	
		if i==len(phoneNumber):
			mnew="".join(new)
			Mset.append(mnew)
		else:
			digit=phoneNumber[i]
			letters=key_mapping[digit]
			for each in letters:
				new[i]=each
				util(i+1,phoneNumber,new,Mset)
	Mset=[]
	new=[0]*len(phoneNumber)
	util(0,phoneNumber,new,Mset)
	return Mset
