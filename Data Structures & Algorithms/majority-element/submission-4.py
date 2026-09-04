class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store=defaultdict(int)
        for s in nums:
            store[s]+=1
        return max(store, key=store.get)