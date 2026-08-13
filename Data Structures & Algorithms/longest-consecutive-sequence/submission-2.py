"""
follow up:
return the sequence itself in order
"""

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
        sequence = []
        for num in nums:
            if num - 1 not in num_set:
                candidate_seq = []
                while num in num_set:
                    candidate_seq.append(num)
                    num += 1
                length = len(candidate_seq)
                if length > longest_length:
                    longest_length = length
                    sequence = candidate_seq
        print(sequence)
        return longest_length
