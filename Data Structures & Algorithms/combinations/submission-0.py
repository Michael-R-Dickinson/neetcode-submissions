'''
appears to be UNIQUE combinations within the range
no possibility of duplication
numbers are already sorted (obviously)

format is as a recurrence relation:
unique_combinations_of_k_numbers_up_to_n(k,n):
    choose to take number n: R(k-1, n-1) + [n] - so add n to all those combinations
    - the combinations STARTING WITH n

    + 

    choose to skip n: R(k, n-1) + []

base cases:
- k == 0 -> we found a combination
- n < 1 -> no combo found
'''



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        def unique_combinations_of_k_numbers_up_to_n(k: int, n: int, current_combo: list[int]):
            if k == 0:
                combos.append(current_combo.copy())
                return
            if n < 1:
                return

            # pick
            current_combo.append(n)
            unique_combinations_of_k_numbers_up_to_n(k-1, n-1, current_combo)
            current_combo.pop()

            # skip
            unique_combinations_of_k_numbers_up_to_n(k, n-1, current_combo)

        combos = []
        unique_combinations_of_k_numbers_up_to_n(k, n, [])
        return combos