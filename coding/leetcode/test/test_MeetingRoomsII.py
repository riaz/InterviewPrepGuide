from src.MeetingRoomsII import Solution

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
    },
    {
        "test_id": "3",
        "input": [[13,15],[1,13]],
        "output": 1
    },
    {
        "test_id": "4",
        "input": [[9,10],[4,9],[4,17]],
        "output": 2
    },
    {
        "test_id": "5",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "6",
        "input": [[2,7]],
        "output": 1
    },
    {
        "test_id": "7",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "8",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "9",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "10",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "11",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "12",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "13",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "14",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "15",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    },
    {
        "test_id": "16",
        "input": [[2,11],[6,16],[11,16]],
        "output": 2
    }
]

class TestSolution:
    def test_minMeetingRooms(self):
        solution = Solution()
        for test in test_cases:
            res = solution.minMeetingRooms(test['input'])
            assert res == test['output']