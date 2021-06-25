"""Take 2 lists and return tuple containing data"""

# from typing import Tuple


def conjunction(list1: list, list2: list) -> list:
    """Find items from both lists"""
    conjlist = []
    sorted(list1)
    sorted(list2)
    for list1_iterate in range(len(list1)):
        for list2_iterate in range(len(list2)):
            if list1[list1_iterate] == list2[list2_iterate]:
                conjlist.append(list2[list2_iterate])
    return sorted(conjlist)


def disjunction(list1: list, list2: list) -> list:
    """Find items from both lists excluding repetitions"""
    sorted(list1)
    sorted(list2)
    disjlist = []
    for list1_iterate in range(len(list1)):
        for list2_iterate in range(len(list2)):
            if list2[list2_iterate] not in disjlist:
                disjlist.append(list2[list2_iterate])
            if list1[list1_iterate] not in disjlist:
                disjlist.append(list1[list1_iterate])
    return sorted(disjlist)


def symdiff(list1: list, list2: list) -> list:
    """Find items from both lists excluding ones items in both sets"""
    symlist = []
    sorted(list1)
    sorted(list2)
    for list1_iterate in range(len(list1)):
        for list2_iterate in range(len(list2)):
            # Symdiff
            if (
                list1[list1_iterate] not in symlist
                and list1[list1_iterate] not in list2
            ):
                symlist.append(list1[list1_iterate])
            if (
                list2[list2_iterate] not in symlist
                and list2[list2_iterate] not in list1
            ):
                symlist.append(list2[list2_iterate])
    return sorted(symlist)


def list2tuple(list1: list, list2: list) -> list:
    """Putting the 3 functions above together"""
    sorted(list1)
    sorted(list2)
    infotuple = (
        conjunction(list1, list2),
        disjunction(list1, list2),
        symdiff(list1, list2),
    )
    return infotuple
