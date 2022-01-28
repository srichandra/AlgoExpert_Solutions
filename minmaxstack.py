# Feel free to add new properties and methods to the class.
class MinMaxStack:
	import math
	def __init__(self):
		self.data=[]
		self.minmaxdata=[]	
    def peek(self):
        return self.data[-1]
        pass

    def pop(self):
		self.minmaxdata.pop()		
        return self.data.pop()

    def push(self, number):
        newminmax={'min':number,'max':number}
		if(len(self.minmaxdata)):
			topminmax=self.minmaxdata[-1]
			newminmax['min']=min(number,topminmax['min'])
			newminmax['max']=max(number,topminmax['max'])
		self.data.append(number)
		self.minmaxdata.append(newminmax)		
        pass
