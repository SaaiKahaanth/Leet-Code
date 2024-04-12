class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # If total gas is less than total cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        
        diff = 0
        start = 0
        for i in range(len(gas)):
            current_tank = gas[i] - cost[i]
            if diff >= 0:
                diff += current_tank
            else:
                diff = current_tank
                start = i
        return start if diff >= 0 else -1
