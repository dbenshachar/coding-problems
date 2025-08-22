### Strategy
# Make a dict with key value pairs count of starting zeroes int to count of memory index | O(n)
# For allocation find

from collections import defaultdict
from typing import List, Tuple


def memory_allocation(memory : List[int], queries : List[Tuple[int, int]]) -> List[int]:
    key = defaultdict(int)
    for l in range(0, len(memory), 8):
        key[(l + 1) // 8] = 0
        r = l
        while l + 8 > r:
            if memory[r] == 0:
                key[(l + 1)// 8] += 1
            else:
                break
            r += 1
    res = []
    for q in queries:
        if q[0] == 0:
            alloc = q[1]
            for idx, mem in key.items():
                if mem >= alloc:
                    for i in range(idx * 8, idx * 8 + 8):
                        memory[i] = 1
                    res.append(idx)
                    alloc = None
                    break

            if alloc is None:
                res.append(-1)

        else:
            pass

    return res

def _run_test(memory : List[int], queries : List[Tuple[int, int]], expected : List[int]):
    result = memory_allocation(memory, queries)
    passed = (result == expected)
    if not passed:
        print(f"For Input: {memory} and {queries} | Expected: {expected} | Recieved: {result}")
        assert passed

if __name__ == "__main__":
    _run_test([0,0,0,0,0,0,0,0,   0,0,1,1,1,1,1,1], [(0,4), (0,2), (0,3), (0,2)], [0, 0, -1, 0])
    # _run_test([0,0,1,1,1,1,1,1, 1,1,1,1,1,1,0,0], [(0,2), (0,3), (1,1), (0,2)], [0, -1, 2, 0])
    # _run_test([0,0,0,0,1,1,1,1,  0,0,0,0,0,0,1,1,  1,1,1,1,0,0,0,0], [(0,3), (0,5), (0,2), (1,2), (1,1)], [0, 8, -1, 5, 3])
