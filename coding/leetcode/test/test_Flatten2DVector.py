from src.Flatten2DVector import Vector2D

test_cases = [
    {
        "test_id": "1",
        "input": {
            "ops": ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"],
            "input": [[1,2],[3],[4]]
        },
        "output": [None, 1, 2, 3, True, True, 4, False]
    }
]

class TestFlatten2DVector:
    def test_flatten2DVector(self):
        for test_case in test_cases:
            print(f"Running {test_case['test_id']}")
            res = []
            for op in test_case["input"]["ops"]:
                if op == "Vector2D":
                    vec = Vector2D(test_case["input"]["input"])
                    res.append(None)
                elif op == "next":
                    res.append(vec.next())
                elif op == "hasNext":
                    res.append(vec.hasNext())
            assert res == test_case["output"]