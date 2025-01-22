import pytest
from solution import Solution


@pytest.mark.parametrize(
    "value, expected",
    [([1, 1, 2], 2), ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)],
)
def test_template(value, expected):
    solution = Solution()
    result = solution.removeDuplicates(value)
    assert result == expected, f"Expected {expected}, got {result}"
