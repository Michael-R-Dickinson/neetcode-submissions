'''
town judge must trust Nobody
- find the person with no edges [person, *]
    - noone satisfies -> no town judge
    - multiple people satisfy -> no town judge
    - one satisfies -> it could be them BUT, we still must check that everyone trusts them

ideas:
- keep an adjacency list: {person: set(who they trust)}
    - building it: O(edges)
    - checking our criteria
        - O(people) -> check who has 0 others they trust (if theres only one satisfying -> candidate judge)
        - O(people) -> check if everyone trusts the candidate judge
            because we're using a set for each one, checking membership is O(1)
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjacency = {i: set() for i in range(1, n + 1)}
        
        # construct adjacency list
        for truster, trustee in trust:
            adjacency[truster].add(trustee)
        
        candidate_judges = [person for person in range(1, n + 1) if len(adjacency[person]) == 0]
        if len(candidate_judges) != 1:
            return -1
        
        candidate_judge = candidate_judges[0]

        for truster, trustees in adjacency.items():
            if truster != candidate_judge and not candidate_judge in trustees:
                return -1

        return candidate_judge
