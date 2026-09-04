class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store={}
        for s in nums:
            store[s]=store.get(s,0)+1
        return max(store, key=store.get)