# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
		self.small=Heap([]) #maxheap
		self.large=Heap([]) #minheap
		
    def insert(self, number):
        # always insert in small heap defau
		self.small.insert(-1*number)
		if self.small.length and self.large.length and ((-1*self.small.peek())>self.large.peek()):
			val=-1*self.small.remove()
			self.large.insert(val)
		#check lens
		if self.small.length>self.large.length+1:
			val=-1*self.small.remove()
			self.large.insert(val)
		if self.large.length>self.small.length+1:
			val=self.large.remove()
			self.small.insert(-1*val)
        pass
		print(self.small.heap,self.large.heap)

    def getMedian(self):
		if self.small.length==self.large.length:
			self.median= (-1*self.small.peek()+self.large.peek())/2
		elif self.small.length>self.large.length:
			self.median= -1*self.small.peek()
		else:
			self.median= self.large.peek()
		return self.median
class Heap: # min heap
	def __init__(self,array):
		self.heap=self.heapify(array)
		self.length=len(self.heap)
	def heapify(self,array):
		lastnonleaf=(len(array)-2)//2
		for i in reversed(range(lastnonleaf+1)):
			self.siftdown(i,len(array)-1,array)
		return array
	def siftdown(self,i,endidx,array):
		l=2*i+1
		while(l<=endidx):
			r=2*i+2 if 2*i+2<=endidx else -1
			if r!=-1 and array[r]<array[l]:
				smallest=r
			else:
				smallest=l
			if array[smallest]<array[i]:
				array[i],array[smallest]=array[smallest],array[ismallest]
				i=smallest
				l=2*i+1
			else:
				return
	def siftup(self,i,array):
		p=(i-1)//2
		while(p>=0):
			if array[i]<array[p]:
				array[p],array[i]=array[i],array[p]
				i=p
				p=(i-1)//2
			else:
				return
	def insert(self,value):
		self.heap.append(value)
		self.length+=1
		self.siftup(self.length-1,self.heap)
	def peek(self):
		return self.heap[0]	
	def remove(self):
		self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
		val=self.heap.pop()
		self.length-=1
		self.siftdown(0,self.length-1,self.heap)
		return val
