class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0
        for s in nums:
            if count==0:
                candidate=s
                count=1
            elif s==candidate:
                count+=1
            else:
                count-=1
        return candidate