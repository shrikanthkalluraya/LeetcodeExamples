# Gas Station (LeetCode #134)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Step 1: Check if a solution is possible
        if len(gas) != len(cost):
            return -1
        total_gas = 0
        total_cost = 0

        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1

        # Step 2: Traverse to find the correct starting station
        start_station = 0
        curr_tank = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            curr_tank += gain
            
            if curr_tank < 0:  # If tank goes negative, restart
                start_station = i + 1
                curr_tank = 0  # Reset tank for new start

        
        # Return the starting station or -1 if not possible
        return start_station
