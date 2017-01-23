class Solution(object):
    def hammingDistance(self, x, y):

        biX = bin(x)[2:]
        biY = bin(y)[2:]
        ll = max(len(biX), len(biY))
        sl = min(len(biX), len(biY))
        if len(biX) <= len(biY):
            biX = '0' * (ll - sl) + biX
        else:
            biY = '0' * (ll - sl) + biY
        n = 0
        for i in xrange(ll):
            if biX[i] != biY[i]:
                n += 1
        return n

    print hammingDistance(1, 1, 17)


class solution283(object):
    def moveZeroes(self, nums):
        index = 0
        size = len(nums)

        for i in range(size):
            if nums[i] == 0:
                continue
            else:
                nums[index] = nums[i]
                index += 1  # index = index+1

        while index < size:
            nums[index] = 0
            index += 1

        return


class Solution1(object):
    def twoSum(self, nums, target):
        index = 0

        return

