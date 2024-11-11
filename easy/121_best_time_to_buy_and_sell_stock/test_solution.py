import pytest
from solution import Solution


@pytest.mark.parametrize(
    "value, expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
)
def test_template(value, expected):
    solution = Solution()
    result = solution.maxProfit(value)
    assert result == expected, f"Expected {expected}, got {result}"
