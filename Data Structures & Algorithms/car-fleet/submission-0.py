class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort both arrays by position
        # calculate arrival time for all indices
        # if arrival time is is <= the next cars arrival time
        # they are in the same fleet

        # x: 4 1 0 7
        # s: 2 2 1 1

        # sorted
        # x: 0  1   4 7
        # s: 1  2   2 1
        # a: 10 9/2 3 3

        cars = [{"position": position[i], "speed": speed[i], "arrival": (target - position[i]) / speed[i]} 
        for i in range(len(position))]
        cars.sort(key=lambda car: car['position'])

        n_fleets = 0
        prev_arrival_time = -1
        for car in reversed(cars):
            if car['arrival'] <= prev_arrival_time:
                # car arrives 'earlier' than the next in line
                # car joins the fleet
                continue
            else:
                # car arrives later than the next in line
                # new fleet created
                # this car becomes the gating arrival time
                n_fleets += 1
                prev_arrival_time = car['arrival']
        return n_fleets
            




        

