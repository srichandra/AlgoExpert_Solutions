class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        perfsum=0
        ans=0
        for num in nums:
            perfsum+=num
            if perfsum-k in d:
                ans = ans + d[perfsum-k]
            if perfsum not in d:
                d[perfsum] = 1  
            else:
                d[perfsum] = d[perfsum]+1
        return ans
