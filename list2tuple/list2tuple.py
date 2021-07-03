"""Take 2 lists and return tuple containing data"""
from typing import Any, List, Tuple


def conjunction(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Find items from both lists"""
    return sorted([i for i in list1 if i in list2])


def disjunction(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Find items from both lists excluding repetitions"""
    return sorted(set(list1 + list2))


def symdiff(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Find items from both lists excluding ones items in both sets"""
    return sorted(
        set(disjunction(list1, list2)) - set(conjunction(list1, list2))
    )


def list2tuple(
    list1: List[Any], list2: List[Any]
) -> Tuple[List[Any], List[Any], List[Any]]:
    """Putting the 3 functions above together"""
    infotuple = (
        conjunction(list1, list2),
        disjunction(list1, list2),
        symdiff(list1, list2),
    )
    return infotuple


# WRITE TEST FOR LIST2TUPLE
