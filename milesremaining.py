def validStartingCity(distances, fuel, mpg):
    minmiles=0
	mincity=0
	milesremaining=0
	for i in range(1,len(distances)):
		milesremaining+=fuel[i-1]*mpg-distances[i-1]
		if(milesremaining<minmiles):
			minmiles=milesremaining
			mincity=i
		
    return mincity
