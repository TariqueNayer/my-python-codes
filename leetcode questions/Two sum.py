class Solution:
    def twoSum(*, nums , target):
        ans = []
        for indi, i in enumerate(nums):
            for indj, j in enumerate(nums):
                if indi == indj or indi > indj:
                    continue
                if i + j == target:
                    ans.append(indi)
                    ans.append(indj)
                    break
        return ans

if __name__ == "__main__":
    sol = Solution
    print(sol.twoSum(nums = [3,2,4], target = 6))