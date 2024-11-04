import pytest
from solution import Solution


@pytest.mark.parametrize(
    "value, expected", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
)
def test_romanToInt(value, expected):
    solution = Solution()
    result = solution.romanToInt(value)
    assert result == expected, f"Expeceted {expected}, got {result}"
