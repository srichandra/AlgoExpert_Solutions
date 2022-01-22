def getNthFib(n):
    Fib=[-1 for x in range(n+1)]
    Fib[0]=0
    Fib[1]=1
	def getfib(n):
        if(Fib[n]!=-1):
			return Fib[n]
		else:
			Fib[n]=getfib(n-1)+getfib(n-2)
			return Fib[n]
	return getfib(n-1)
    pass
