class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = candidate = tank = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            total += net
            tank += net

            if tank < 0:
                candidate = i + 1
                tank = 0
        
        return candidate if total >= 0 else -1