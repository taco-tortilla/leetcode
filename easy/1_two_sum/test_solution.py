import pytest
from solution import Solution


@pytest.mark.parametrize(
    "value, target, expected",
    [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])],
)
def test_twoSum(value, target, expected):
    solution = Solution()
    result = solution.twoSum(value, target)
    assert result == expected, f"Expected {expected}, got {result}"
