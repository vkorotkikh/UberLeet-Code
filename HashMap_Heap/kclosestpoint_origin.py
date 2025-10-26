import os
import heapq
from typing import List

# ------------------------------------------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------------------------------------------

TEST_CASES = [
    ([[1,3],[-2,2]], 1),
    ([[3,3],[5,-1],[-2,4]], 2),
]

"""
You are given a 2D array points, where points[i] = [xi, yi] represents the coordinates of a point on an
X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""