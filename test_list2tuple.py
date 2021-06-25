import pytest
import list2tuple as lt

# testlist1 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# testlist2 -> 0, 1, 2, 3, 6, 7, 8, 9, 13, 15
testlist1 = [1, 3, 2, 6, 5, 9, 8, 0, 7, 4]
testlist2 = [6, 9, 1, 2, 3, 0, 15, 13, 7, 8]
testlist3 = []


def test_conjunction():
    got = lt.conjunction(testlist1, testlist2)
    expected = [0, 1, 2, 3, 6, 7, 8, 9]
    assert got == expected


def test_disjunction():
    got = lt.disjunction(testlist1, testlist2)
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 15]
    assert got == expected


def test_symdiff():
    got = lt.symdiff(testlist1, testlist2)
    expected = [4, 5, 13, 15]
    assert got == expected
