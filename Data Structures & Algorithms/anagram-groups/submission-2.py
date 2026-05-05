class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        print(ana)

        for i in strs:
            j = "".join(sorted(i))  
            ana[j].append(i)
        print(ana)
        return ana.values()
            
        