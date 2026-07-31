
'''

'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        def addCombinations(nums_idx: int, target: int, current_state: list) -> None:
            '''
            add all combinations of numbers in nums[nums_idx:] that add up to target to combos list. 
            current_state is the current combination that led to the reduced target value
            - used as the base combination we add onto to create combos that add to target

            Note: current_state is passed by object reference - must be kept updated rather than copied, except when adding to the output

            returns: None - only side effect
            '''

            if target == 0:
                # add to combos
                combos.append(current_state.copy())
                return
            if target < 0:
                # bad combo - return
                return
            if nums_idx == len(nums):
                # we've run out of numbers
                # no combo found
                return
            
            # 2 options
            
            # choose current num - keep nums_idx unchanged - we can use it again
            # temporarily add to current state - single object reference
            current_state.append(nums[nums_idx])
            addCombinations(nums_idx, target-nums[nums_idx], current_state)
            current_state.pop()

            # skip this number - we cannot use it again
            addCombinations(nums_idx + 1, target, current_state)
        addCombinations(0, target, [])
        return combos








