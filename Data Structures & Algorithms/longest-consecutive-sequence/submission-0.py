class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        longest=0
        for num in n:
            if num-1 not in n:
                l=1
                while num+l in n:
                    l+=1
                longest=max(longest,l)
        return longest

