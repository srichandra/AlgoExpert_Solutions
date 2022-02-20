class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts=[0]*n
        trusted=[0]*n
        for each in trust:
            trusts[each[0]-1]+=1
            trusted[each[1]-1]+=1
        for i in range(n):
            if trusts[i]==0 and trusted[i]==n-1:
                return i+1
        return -1
        
