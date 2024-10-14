class Solution:
    def to_binary(self, num):
        return bin(num)[2:]
    
    def binarysort(self, binaries):
        bistr1 = binaries[0] + binaries[1]
        bistr2 = binaries[1] + binaries[0]
        if bistr2 > bistr1:
            binaries[0], binaries[1] = binaries[1], binaries[0]

        bistr1 = binaries[0] + binaries[2]
        bistr2 = binaries[2] + binaries[0]
        if bistr2 > bistr1:
            binaries[0], binaries[2] = binaries[2], binaries[0]

        bistr1 = binaries[1] + binaries[2]
        bistr2 = binaries[2] + binaries[1]
        if bistr2 > bistr1:
            binaries[1], binaries[2] = binaries[2], binaries[1]

        return binaries 

    def max_binary_concat(self, nums):
        binaries = [self.to_binary(num) for num in nums]
        print(binaries)
        binaries = self.binarysort(binaries)
        print(binaries)
        max_binary_str = ''.join(binaries)
        return int(max_binary_str, 2)

nums = [110,30,1]
sol = Solution()
result = sol.max_binary_concat(nums)
print(f"Max decimal value: {result}")

