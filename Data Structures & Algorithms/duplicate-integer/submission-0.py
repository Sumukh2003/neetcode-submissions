class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        there=set()
        for i in nums:
            if i in there:
                return True
            there.add(i)
        return False
