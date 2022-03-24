class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        size=len(people)
        heavy=size-1
        light=0
        boat=0
        while (light<=heavy):
            if light==heavy:
                boat=boat+1
                light=light+1
                
            elif people[light]+people[heavy] <=limit:
                heavy=heavy-1
                light=light+1
                boat=boat+1
            else:
                boat=boat+1
                heavy=heavy-1
        return boat
            
        