def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    def retspeed(a,b):
		count=0
		for i in range(len(a)):
			count+=max(a[i],b[i])
		return count
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	if(fastest):
		return retspeed(redShirtSpeeds,blueShirtSpeeds[::-1])
	else:
		return retspeed(redShirtSpeeds,blueShirtSpeeds)
