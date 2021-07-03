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


def test_emptyconjunction():
    got = lt.conjunction(testlist1, testlist3)
    expected = []
    assert got == expected


def test_sameconjunction():
    got = lt.conjunction(testlist1, testlist1)
    expected = sorted(testlist1)
    assert got == expected


def test_disjunction():
    got = lt.disjunction(testlist1, testlist2)
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 15]
    assert got == expected


def test_emptydisjunction():
    got = lt.disjunction(testlist1, testlist3)
    expected = sorted(testlist1)
    assert got == expected


def test_samedisjunction():
    got = lt.disjunction(testlist1, testlist1)
    expected = sorted(testlist1)
    assert got == expected


def test_symdiff():
    conj = lt.conjunction(testlist1, testlist2)
    assert conj == [0, 1, 2, 3, 6, 7, 8, 9]
    got = lt.symdiff(testlist1, testlist2)
    expected = [4, 5, 13, 15]
    assert got == expected


def test_emptysymdiff():
    got = lt.symdiff(testlist1, testlist3)
    expected = sorted(testlist1)
    assert got == expected


def test_samesymdiff():
    got = lt.symdiff(testlist1, testlist1)
    expected = []
    assert got == expected

# WRITE TEST FOR LIST2TUPLE
