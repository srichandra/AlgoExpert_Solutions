def spiralTraverse(array):
	res=[]
    sr=0
	er=len(array)-1
	sc=0
	ec=len(array[0])-1
	while((sr<=er) and (sc<=ec)):
		for col in range(sc,ec+1):
			res.append(array[sr][col])
		for row in range(sr+1,er+1):
			res.append(array[row][ec])
		for col in reversed(range(sc,ec)):
			if(sr==er):
				break
			res.append(array[er][col])
		for row in reversed(range(sr+1,er)):
			if sc==ec:
				break
			res.append(array[row][sc])
		sc+=1
		ec-=1
		sr+=1
		er-=1
	return res
		
    pass
