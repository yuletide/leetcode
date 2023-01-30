import pytest
from leetcode_encode_strings.encode_strings import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["hello", "world"], 8),
        (["with#2", "34234234"], 6),
        (["Lots#*", "(*&2347", "specialchars@ü"], 42),
    ],
)
def test_solution_case(test_input, expected):
    str = test_input
    solution = Solution()
    encoded = solution.encode(str)
    assert test_input == solution.decode(encoded)
