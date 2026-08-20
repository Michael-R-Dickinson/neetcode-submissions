'''
important constraint: uniqueness! and each element can only be used once!


combinationsThatSumToTarget(nums, target):
    choose the first number: combinationsThatSumToTarget(nums[1:], target - nums[0], current_combo)
    + 
    skip the first number:
    combinationsThatSumToTarget(nums[1:], target, current_combo)

base case for combinationsThatSumToTarget()
- target < 0 -> 0 combinations
- target = 0 -> we found a combination -> add to set
- len(nums) == 0 -> no combination

'''



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationsThatSumToTarget(nums_idx, target, current_combo):
            if target < 0:
                return
            if target == 0:
                combos.append(current_combo[:])
                return
            if nums_idx == len(candidates):
                return

            # choose
            current_combo.append(candidates[nums_idx])
            combinationsThatSumToTarget(nums_idx + 1, target - candidates[nums_idx], current_combo)
            current_combo.pop()

            # skip
            i = 1
            while nums_idx + i < len(candidates) and candidates[nums_idx + i] == candidates[nums_idx]:
                i += 1
            combinationsThatSumToTarget(nums_idx + i, target, current_combo)

        already_computed = set()
        combos = []
        candidates = sorted(candidates)
        combinationsThatSumToTarget(0, target, [])
        return combos


        