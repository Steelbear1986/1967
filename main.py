class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        from collections import Counter
        patterns= Counter(patterns)
        ans=0
        for i,n in patterns.items():
            if i in word:
                ans+=n
        return ans