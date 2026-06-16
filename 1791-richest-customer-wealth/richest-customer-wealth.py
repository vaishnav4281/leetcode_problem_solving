class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = [0] * len(accounts)
        for i in range(len(accounts)):
            res[i] = sum(accounts[i])
        return max(res)
            

