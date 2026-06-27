class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # pair heaviest + lightest
        boat_count = 0
        heaviest = len(people) - 1
        lightest = 0
        while lightest <= heaviest:
            if people[lightest] + people[heaviest] <= limit:
                boat_count += 1
                lightest += 1
                heaviest -= 1
            else:
                boat_count += 1
                heaviest -= 1
        return boat_count