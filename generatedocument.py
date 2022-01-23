def generateDocument(characters, document):
    characters_map={}
	for each in characters:
		characters_map[each]=characters_map.get(each,0)+1
	document_map={}
	for each in document:
		document_map[each]=document_map.get(each,0)+1
	for each in document:
		if((characters_map.get(each,0)-document_map[each])<0):
			return False
    return True
