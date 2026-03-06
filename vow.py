class Solution:
    def sortVowels(self, s: str) -> str:
        t,l,k="",[],0
        l=[i for i in s if i in "aeiouAEIOU"]
        l.sort()
        for i in s:
            if i in "aeiouAEIOU":
                t+=l[k]
                k+=1
            else:
                t+=i
        return t
