class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s1 = set()
        r = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in s1:
                r.add(seq)
            else:
                s1.add(seq)
        return list(r)
