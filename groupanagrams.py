def groupAnagrams(words):
	res={}
    for each in words:
		sortedw="".join(sorted(each))
		if sortedw in res:
			res[sortedw].append(each)
		else:
			res[sortedw]=[each]
	return list(res.values())
    pass
