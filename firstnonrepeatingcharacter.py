def firstNonRepeatingCharacter(string):
    # Write your code here.
	hash_map={}
	for each in string:
		hash_map[each]=hash_map.get(each,0)+1
	for i,each in enumerate(string):
		if(hash_map[each]==1):
			return i			
    return -1
