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
