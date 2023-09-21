import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
            Sort the list by start and end-times [[0,30], [5, 10], [15, 20]]
            max_room = 0
            rooms_ends = [] - use a heap (min-heap)
            for scehedule in schedules:
                for room in room_end:
                    if room < shedule.start:
                        remove(room)
                        add(schedule_start)
                    


        """
        max_rooms = 0
        intervals.sort()
        rooms = []
        for (start, end) in intervals:
            if not rooms:
                heapq.heappush(rooms, end)
            else:
                # check if the quickest to finish meetings (as we heap with end) is less than start of next
                if rooms[0] <= start:
                    # we will pop the quickest to end meet                                        
                    heapq.heappop(rooms)
                # add the end of current meet                    
                heapq.heappush(rooms, end)

            max_rooms = max(max_rooms, len(rooms))
        return max_rooms        