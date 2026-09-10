class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ne=list()
        for s in strs:
            for sub in ne:
                if sorted(s)==sorted(sub[0]):
                    sub.append(s)
                    break
            else:
                ne.append([s])
        return ne