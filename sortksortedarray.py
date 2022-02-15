class MinHeap():
	def __init__(self,nums):
		self.nums=self.heapify(nums)
	def heapify(self,nums):
		lastnonleaf=(len(nums)-2)//2
		for i in reversed(range(lastnonleaf+1)):
			self.siftdown(i,len(nums)-1,nums)
		return nums
	def siftdown(self,i,endidx,heap):
		l=2*i+1
		while(l<=endidx):
			r=2*i+2 if 2*i+2<=endidx else -1
			if r!=-1 and heap[r]<heap[l]:
				smallest=r
			else:
				smallest=l
			if heap[smallest]<heap[i]:
				heap[smallest],heap[i]=heap[i],heap[smallest]
				i=smallest
				l=2*i+1
			else:
				return
	def siftup(self,i,heap):
		p=(i-1)//2
		while(p>=0):
			if heap[i]<heap[p]:
				heap[p],heap[i]=heap[i],heap[p]
				i=p
				p=(i-1)//2
			else:
				return
	def insert(self,val):
		self.nums.append(val)
		self.siftup(len(self.nums)-1,self.nums)
	def ret(self):	
		self.nums[0],self.nums[-1]=self.nums[-1],self.nums[0]
		val=self.nums.pop()
		self.siftdown(0,len(self.nums)-1,self.nums)
		return val
def sortKSortedArray(array, k):
	H=MinHeap(array[:min(k+1,len(array))])
	i=k+1
	res=[]
	print(H.nums)
	while(i<len(array)):
		res.append(H.ret())
		H.insert(array[i])
		i+=1
	
	while(len(H.nums)>0):
		res.append(H.ret())
	return res
