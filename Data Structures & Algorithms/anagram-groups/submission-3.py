class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)

        for word in strs:
            arr=[0]*26
            for c in word:
                arr[ord(c)-ord('a')]+=1
            ana[tuple(arr)].append(word)
        res=[]
        for key,value in ana.items():
            res.append(value)
        return res


        