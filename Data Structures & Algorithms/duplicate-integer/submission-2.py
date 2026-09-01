class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dih=set()
        for i in nums:
            if i in dih:
                return True
            dih.add(i)
        return False