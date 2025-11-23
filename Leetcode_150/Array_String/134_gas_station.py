class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # m = len(cost)

        if len(gas) != len(cost):
            return -1
        
        if sum(gas) < sum(cost):
            return -1
            
        # Step 2: Traverse to find the correct starting station
        start_station = 0
        curr_tank = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            curr_tank += gain
            print(gain, curr_tank)
            if curr_tank < 0:  # If tank goes negative, restart
                start_station = i + 1
                curr_tank = 0  # Reset tank for new start

        
        # Return the starting station or -1 if not possible
        return start_station
