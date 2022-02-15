def laptopRentals(times):
	if len(times)==0:
		return 0
	count=0
	atimes=sorted([time[0] for time in times])
	dtimes=sorted([time[1] for time in times])
	a=0
	d=0
	count=0
	max
	n=len(times)
	while a<n:
		if atimes[a]>=dtimes[d]:
			count-=1
			d+=1
		count+=1
		a+=1
	return count
