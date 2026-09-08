class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n//2):
            min=i
            max=i
            for j in range(0+i,n-i):
                if nums[min]>nums[j]:
                    min=j
                if nums[max]<nums[j]:
                    max=j
            if max==i:
                max=min
            nums[min],nums[i]=nums[i],nums[min]
            nums[max],nums[n-1-i]=nums[n-1-i],nums[max]
        return nums