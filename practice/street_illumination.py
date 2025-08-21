"""
Problem: Brightest Position on Street
A street is represented by a number line. You are given an integer n representing the number of street lamps, and a 2D array lamps where each lamps[i] = [position_i, range_i]:
Each lamp is placed at position_i on the street.
The lamp illuminates every position p where position_i - range_i <= p <= position_i + range_i.
The illumination of a position p is defined as the number of lamps that illuminate that position.
Return the position on the street that has the maximum illumination. If there are multiple such positions, return the smallest one.
Example 1
Input:
lamps = [[-3,2],[1,2],[3,3]]
Output:
1
Explanation:
Lamp 1 at -3 covers [-5, -1]
Lamp 2 at 1 covers [-1, 3]
Lamp 3 at 3 covers [0, 6]
Position 1 is illuminated by 2 lamps, and no position is illuminated by more than 2 lamps.
Example 2
Input:
lamps = [[1,0],[0,1]]
Output:
0
Explanation:
Lamp 1 at 1 covers [1,1]
Lamp 2 at 0 covers [-1,1]
Position 0 is illuminated by both lamps, so it has the maximum illumination.
"""

from typing import List
from collections import defaultdict

def street_illumination(lamps : List[List[int]]) -> int:
    starts = defaultdict(int)
    ends = defaultdict(int)
    points = set()
    for pos, rad in lamps:
        starts[pos - rad] += 1
        ends[pos + rad] += 1
        points.add(pos - rad)
        points.add(pos + rad)
    points = sorted(points)

    illuminated = 0
    best = 0
    res = 0
    for p in points:
        illuminated += starts[p]
        if illuminated > best:
            best = illuminated
            res = p
        illuminated -= ends[p]
    return res

def _run_test(lamps : List[List[int]], expected : int):
    result = street_illumination(lamps)
    passed = (result == expected)
    if not passed:
        print(f"For Lamps: {lamps} | Expected: {expected} | Recieved: {result}")
        assert passed

if __name__ == "__main__":
    _run_test([[-3,2],[1,2],[3,3]], -1)
    _run_test([[1, 0], [0, 1]], 1)