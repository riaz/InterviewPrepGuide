from typing import List

def bin_search(lst: List[int], lo: int, hi: int, e: int) -> int:
    if lo > hi:
        return -1    
    mid  = lo + (hi - lo) // 2

    if lst[mid] == e:
        return mid
    elif lst[mid] < e:
        return bin_search(lst, lo, mid-1, e)
    else:
        return bin_search(lst, mid+1, hi, e)


if __name__ == "__main__":
    lst =  [3,4,1,2,5,6,7,8,9,10]
    
    lst.sort()

    print(lst)
    
    assert bin_search(lst, 0, len(lst)-1, 5) > 0

    assert bin_search(lst, 0, len(lst)-1, -1) == -1