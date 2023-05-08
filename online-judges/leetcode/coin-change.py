# https://leetcode.com/problems/coin-change/


class Solution:
    def change(self, coins, amount, cache):
        if amount in cache:
            return cache[amount]

        if amount == 0:
            return 0

        ncoins = float("inf")
        for coin in coins:
            if coin > amount:
                continue

            if amount % coin == 0:
                used = amount // coin
                subchange = self.change(coins, amount % coin, cache)
            else:
                used = 1
                subchange = self.change(coins, amount - coin, cache)

            if subchange != -1:
                ncoins = min(ncoins, used + subchange)

        cache[amount] = ncoins if ncoins != float("inf") else -1
        return cache[amount]

    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.change(coins, amount, dict())


# Tests
solver = Solution()
assert solver.coinChange([1, 2, 5], 11) == 3
assert solver.coinChange([2], 3) == -1
assert solver.coinChange([1], 0) == 0
assert solver.coinChange([1, 2, 5], 100) == 20
assert solver.coinChange([186, 419, 83, 408], 6249) == 20
