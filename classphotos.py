def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
	blueShirtHeights.sort()
	valid=True
	i=0
	while((i<len(redShirtHeights)) & valid):
		if(redShirtHeights[i]==blueShirtHeights[i]):
			return False
		sign=(redShirtHeights[i]-blueShirtHeights[i])<0
		if(i==0):
		  prev=sign
		else:
		  if(prev!=sign):
		  	valid=False		  
		i+=1
    return valid
