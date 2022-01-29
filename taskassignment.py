def taskAssignment(k, tasks):
    # Write your code here.
	taskidx={}
	for i,each in enumerate(tasks):
		if each in taskidx:
			taskidx[each].append(i)
		else:
			taskidx[each]=[i]
	sorted_tasks=sorted(tasks)
	pairs=[]
	start=0
	end=len(tasks)-1
	while(start<end):
		task1dur=sorted_tasks[start]
		task1idx=taskidx[task1dur].pop()
		
		task2dur=sorted_tasks[end]
		task2idx=taskidx[task2dur].pop()
		
		start+=1
		end-=1

		pairs.append([task1idx,task2idx])
	return pairs
