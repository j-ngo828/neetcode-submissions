class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set
        num_set = set(nums)

        # scan left to right in nums
        # if num - 1 not in set, num is
        # a start of a sequence,
        # keep finding num + 1 and record length
        # compare length with global longest length
        # so far
        # return global longest length
        longest_length = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while num in num_set:
                    length += 1
                    num += 1
                longest_length = max(
                    longest_length,
                    length,
                )
        return longest_length
