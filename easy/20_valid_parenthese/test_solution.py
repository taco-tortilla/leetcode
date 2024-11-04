import pytest
from solution import Solution


@pytest.mark.parametrize(
    "value, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("((", False),
        ("){", False),
        ("(){}}{", False),
        ("(", False),
        (")", False),
    ],
)
def test_isValid(value, expected):
    solution = Solution()
    result = solution.isValid(value)
    assert result == expected, f"Expected {expected}, got {result}"
