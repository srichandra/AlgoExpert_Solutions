# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstparent=(len(array)-2)//2
		for i in reversed(range(firstparent+1)):
			self.siftDown(i,len(array)-1,array)
		return array
    def siftDown(self,currind,endidx,heap):
        l=2*currind+1
		while l<=endidx:
			r=2*currind+2 if 2*currind+2<endidx else -1
			if r!=-1 and heap[r]<heap[l]:
				smallest=r
			else:
				smallest=l
			if heap[smallest]<heap[currind]:
				self.swap(smallest,currind,heap)
				currind=smallest
				l=2*currind+1
			else:
				return
        pass

    def siftUp(self,currindx,heap):
		p=(currindx-1)//2
		while currindx>0 and heap[currindx]<heap[p]:
			self.swap(currindx,p,heap)
			currindx=p
			p=(currindx-1)//2

    def peek(self):
		self.siftUp(len(self.heap)-1,self.heap)
        return self.heap[0]


    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
		valueToRemove=self.heap.pop()
		self.siftDown(0,len(self.heap)-1,self.heap)
		return valueToRemove

    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap)-1,self.heap)
        pass
	
	def swap(self,i,j,heap):
        heap[i],heap[j]=heap[j],heap[i]
