from typing import List

class Vector2D:
    
    def __init__(self, vec: List[List[int]]):
        """
        Read vec and flatten it out in the constuctor
        """
        self.flatten = []
        for lst in vec:
            self.flatten.extend(lst)
        self.idx = 0

    def next(self) -> int:
        """
        This is should use yield probably
        """
        val = self.flatten[self.idx]
        self.idx+=1
        return val

        

    def hasNext(self) -> bool:
        return self.idx < len(self.flatten)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()