# Can complete the circuit # LeetCode #134
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
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
        if total_gas != total_cost:
            return -1

        # Step 2: Traverse to find the correct starting station
        start_station = -1       
        for i in range(len(gas)):
            if gas[i]<cost[i]:
                start_station = i



        
        # Return the starting station or -1 if not possible
        return start_station
