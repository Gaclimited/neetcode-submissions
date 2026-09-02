class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ne={}
        for s in strs:
            key=''.join(sorted(s))
            if key in ne:
                ne[key].append(s)
            else:
                ne[key]=[s]
        return list(ne.values())