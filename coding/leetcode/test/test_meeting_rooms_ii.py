from src.meeting_rooms_ii import Solution

test_cases = [
    {
        "test_id": "1",
        "input": [[0,30],[5,10],[15,20]],
        "output": 2
    },
    {
        "test_id": "2",
        "input": [[7,10],[2,4]],
        "output": 1
    }
]

class TestSolution:
    def test_minMeetingRooms(self):
        solution = Solution()
        for test in test_cases:
            print(f"Running test: {test['test_id']}")
            res = solution.minMeetingRooms(test['input'])
            assert res == test['output']

