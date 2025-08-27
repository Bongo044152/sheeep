# file: tests/test_exercises.py

import pytest

from exercises.ex_branching import grade
from exercises.ex_loops import sum_1_to_n, find_max
from exercises.ex_strings import reverse_words, count_vowels


# ---------- ex_branching.py ----------
@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
    ],
)
def test_grade(score, expected):
    assert grade(score) == expected


# ---------- ex_loops.py ----------
@pytest.mark.parametrize("n", [0, 1, 2, 5, 10, 100])
def test_sum_1_to_n(n):
    assert sum_1_to_n(n) == n * (n + 1) // 2

def test_find_max_basic():
    assert find_max([3, 9, -1, 7]) == 9
    assert find_max([-5, -2, -9]) == -2
    assert find_max([42]) == 42

def test_find_max_empty_raises():
    with pytest.raises(Exception):
        find_max([])

# ---------- ex_strings.py ----------
@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello world", "world hello"),
        ("a b c", "c b a"),
        ("single", "single"),
        ("  spaced   words ", "words spaced"),
    ],
)
def test_reverse_words(s, expected):
    assert reverse_words(s) == expected

@pytest.mark.parametrize(
    "s, expected",
    [
        ("Programming", 3),  # o, a, i
        ("AEIOU", 5),
        ("xyz", 0),
        ("Rhythm", 0),       # y 不是母音
        ("Mixed CASE", 4),   # i, e, A, E
    ],
)
def test_count_vowels(s, expected):
    assert count_vowels(s) == expected
