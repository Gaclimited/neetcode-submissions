class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=0
        for i in range(0, len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]==nums[j]:
                    s+=1
        return (bool(s))