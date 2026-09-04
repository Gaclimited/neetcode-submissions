class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        store={}
        for s in nums:
            store[s]=store.get(s,0)+1
        return max(store, key=store.get)