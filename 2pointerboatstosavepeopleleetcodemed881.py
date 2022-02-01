from typing import List
# If sorted arry is given use two pinters
# if array is not sorted try to sort and then approach problem
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        size = len(people)
        heavy = size - 1
        light = 0
        boat = 0
        while (light <= heavy):
            if light == heavy:
                boat = boat + 1
                light = light + 1

            elif people[light] + people[heavy] <= limit:
                heavy = heavy - 1
                light = light + 1
                boat = boat + 1
            else:
                boat = boat + 1
                heavy = heavy - 1
        return boat
s=Solution()
people=[3,2,2,1]
limit=3
ans=s.numRescueBoats(people,limit)
print(ans)