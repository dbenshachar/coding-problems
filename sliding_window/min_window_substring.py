### Strategy
# Make a dict with key value pairs count of starting zeroes int to count of memory index | O(n)
# For allocation find

from collections import defaultdict
from typing import List, Tuple


def memory_allocation(arr1 : str, arr2 : str) -> str:
    return ""

def _run_test(arr1 : str, arr2 : str, expected : str):
    result = memory_allocation(arr1, arr2)
    passed = (result == expected)
    if not passed:
        print(f"For Input: {arr1} and {arr2} | Expected: {expected} | Recieved: {result}")
        assert passed

if __name__ == "__main__":
    _run_test("ahffaksfajeeubsne", "jefaa", "aksfaje")
    _run_test("aaffhkksemckelloe", "fhea", "affhkkse")