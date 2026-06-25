class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = list(nums)
        for i in range(1, len(output)):
            output[i] = output[i - 1] * nums[i]
        suffix_product = 1
        # [1, 2, 8, 8]
        #        i
        # suffix_product = 6
        for i in range(len(output) - 1, -1, -1):
            output[i] = suffix_product * (output[i - 1] if i - 1 >= 0 else 1)
            suffix_product *= nums[i]
        return output
