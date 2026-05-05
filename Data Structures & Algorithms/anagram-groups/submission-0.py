class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sorteds=''.join(sorted(s))
            print(sorteds)
            res[sorteds].append(s)
            print(res)
        return list(res.values())

        