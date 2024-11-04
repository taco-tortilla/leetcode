import pytest
from solution import Solution


@pytest.mark.parametrize(
    "value, expected",
    [(121, True), (-121, False), (10, False)],
)
def test_isPalindrome(value, expected):
    solution = Solution()
    result = solution.isPalindrome(value)
    assert result == expected, f"Expected {expected}, got {result}"
