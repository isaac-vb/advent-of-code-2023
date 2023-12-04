import pytest
from day3 import check_horizontal_adjacency, check_vertical_adjacency, check_diagonal_adjacency


@pytest.fixture
def digits_and_symbols_horizontal():
    return [
        (('123', [0, 1, 2], 5), ('*', [3], 5), 123),
        (('123', [1, 2, 3], 5), ('*', [0], 5), 123),
        (('12', [0, 1], 5), ('*', [2], 5), 12),
        (('12', [3, 4, 5], 5), ('*', [2], 5), 12),
        (('1', [0], 5), ('*', [1], 5), 1),
        (('1', [17], 5), ('*', [16], 5), 1)
    ]


def test_check_horizontal_adjacency(digits_and_symbols_horizontal):
    for digits_tuple, symbols_tuple, expected_result in digits_and_symbols_horizontal:
        result = check_horizontal_adjacency(digits_tuple, symbols_tuple)
        assert result == expected_result


@pytest.fixture
def digits_and_symbols_vertical():
    return [
        # Below for any 3 digit number
        (('123', [0, 1, 2], 6), ('*', [0], 7), 123),
        (('123', [0, 1, 2], 6), ('*', [1], 7), 123),
        (('123', [0, 1, 2], 6), ('*', [2], 7), 123),
        # Above for any 3 digit number
        (('123', [0, 1, 2], 6), ('*', [0], 5), 123),
        (('123', [0, 1, 2], 6), ('*', [1], 5), 123),
        (('123', [0, 1, 2], 6), ('*', [2], 5), 123),
        # Below for any 2 digit number
        (('12', [6, 7], 6), ('*', [6], 7), 12),
        (('12', [6, 7], 6), ('*', [7], 7), 12),
        # Above for any 2 digit number
        (('12', [10, 11], 6), ('*', [10], 5), 12),
        (('12', [10, 11], 6), ('*', [11], 5), 12),
        # Below for any 1 digit number
        (('1', [100], 8), ('*', [100], 9), 1),
        # Above for any 1 digit number
        (('1', [100], 6), ('*', [100], 5), 1)

    ]


def test_check_vertical_adjacency(digits_and_symbols_vertical):
    for digits_tuple, symbols_tuple, expected_result in digits_and_symbols_vertical:
        result = check_vertical_adjacency(digits_tuple, symbols_tuple)
        assert result == expected_result


@pytest.fixture
def digits_and_symbols_diagonal():
    return [
        # Diagonal adjacency for a 3-digit number
        (('123', [10, 11, 12], 2), ('*', [9], 1), 123),
        # Diagonal adjacency for a 3-digit number at the upper boundary
        (('123', [0, 1, 2], 6), ('*', [0], 7), 123),
        (('123', [0, 1, 2], 6), ('*', [1], 7), 123),
        (('123', [0, 1, 2], 6), ('*', [2], 7), 123),
        # Diagonal adjacency for a 3-digit number at the lower boundary
        (('123', [0, 1, 2], 6), ('*', [0], 5), 123),
        (('123', [0, 1, 2], 6), ('*', [1], 5), 123),
        (('123', [0, 1, 2], 6), ('*', [2], 5), 123),
        # Diagonal adjacency for a 2-digit number
        (('12', [6, 7], 6), ('*', [6], 7), 12),
        (('12', [6, 7], 6), ('*', [7], 7), 12),
        # Diagonal adjacency for a 2-digit number at the upper boundary
        (('12', [10, 11], 6), ('*', [10], 5), 12),
        (('12', [10, 11], 6), ('*', [11], 5), 12),
        # Diagonal adjacency for a 1-digit number
        (('1', [100], 8), ('*', [100], 9), 1),
        # Diagonal adjacency for a 1-digit number at the lower boundary
        (('1', [100], 6), ('*', [100], 5), 1)
    ]


def test_check_diagonal_adjacency(digits_and_symbols_diagonal):
    for digits_tuple, symbols_tuple, expected_result in digits_and_symbols_diagonal:
        result = check_diagonal_adjacency(digits_tuple, symbols_tuple)
        assert result == expected_result
