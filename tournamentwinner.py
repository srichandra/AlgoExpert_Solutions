def tournamentWinner(competitions, results):
    points_dict={}
	max_val=0
	max_key=''
	for i in range(len(results)):
		points_dict[competitions[i][1-results[i]]]=points_dict.get(competitions[i][1-results[i]],0)+3
		if(points_dict.get(competitions[i][1-results[i]],0)>max_val):
			max_val=points_dict.get(competitions[i][1-results[i]],0)
			max_key=str(competitions[i][1-results[i]])		
    return max_key
