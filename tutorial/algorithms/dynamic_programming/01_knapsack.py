
from typing import List

def knapsack_naive(W: int, wt: List[int], val: List[int], n: int) -> int:
    if n == 0 or W == 0:
        return 0
    return 0

if __name__ == '__main__':
    scores = [100, 60, 120] # score
    weights = [20, 10, 30] # weight
    
    # we need to jointly sort weights and columns
    weights, scores = map(list, zip(*[(w,s) for w, s in sorted(zip(weights, scores), 
                                                    key=lambda pair: pair[0])]))

    print(weights, scores)

    print(list(zip([(1,2), (3,4)])))
    print(list(zip(*[(1,2), (3,4)])))
    
    
    W = 50 
    N = len(scores)

    print(knapsack_naive(W, weights, scores, N))

    # we will be using knapsack algorithm to pick weights that is <= 50, that maximizes the score
    # for example for the above example 
