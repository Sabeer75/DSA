class Solution:
    def startStation(self, gas, cost):
        #  code here
        if sum(gas) < sum(cost):
            return -1

        curr = 0
        start = 0

        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0

        return start
