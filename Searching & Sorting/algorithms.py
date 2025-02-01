
"""Implementations of some sorting"""
import random
from Interfaces import List

def linear_search(a: List, x: object):
    """\n    uses the linear search algorithm to return the index of the given\n    element if it is found in the given list; otherwise returns None.\n    :param a: List subclass type; an object from a class that implements the List interface\n    :param x: object type; the object to search for\n    """  # inserted
    for i in range(a.size()):
        if a[i] == x:
            return i
    else:  # inserted
        return None


def binary_search(a: List, x: object):
    """
    Uses the binary search algorithm to return the index of the given
    element if it is found in the given SORTED list; otherwise returns None.
    
    :param a: List to search in (must be sorted)
    :param x: Element to search for
    :return: Index of element if found, None otherwise
    """
    left = 0
    right = len(a) - 1  
    
    while left <= right:
        mid_idx = (left + right) // 2 
        
        try:
            mid_ele = a[mid_idx]
        except (TypeError, IndexError):
            return None
            
        if mid_ele == x:
            return mid_idx
        elif x < mid_ele:  
            right = mid_idx - 1  
        else:
            left = mid_idx + 1  #
    
    return None
def _merge(a0: List, a1: List, a: List):
    """\n    helper method to merge_sort(); merges list a0 and a1 into\n    sorted list a\n    """  # inserted
    i0 = 0
    i1 = 0
    for i in range(a.size()):
        if i0 >= a0.size():
            a[i] = a1[i1]
            i1 = i1 + 1
        else:  # inserted
            if i1 >= a1.size():
                a[i] = a0[i0]
                i0 = i0 + 1
            else:  # inserted
                if a0[i0] <= a1[i1]:
                    a[i] = a0[i0]
                    i0 = i0 + 1
                else:  # inserted
                    if a1[i1] < a0[i0]:
                        a[i] = a1[i1]
                        i1 = i1 + 1

def merge_sort(a: List):
    """\n    sorts the given list\n    :param a: List subclass type; an object from a class that implements the List interface\n    """  # inserted
    if a.size() <= 1:
        return
    mid = a.size() // 2
    a0 = a[:mid]
    a1 = a[mid:]
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)



def _partition_f(a: List, start: int, end: int) -> int:
    """\n    helper method to _quick_sort_f(); partitions a sublist of the given list\n    using the first element of the sublist as pivot. The elements of the sublist\n    are arranged into two groups: the first group consists of elements\n    that are less than or equal to the pivot. The second group is\n    a group of elements that are greater than the pivot.  By the end of the\n    partitioning process, the pivot is placed in its correct, sorted order,\n    elements in the first group appear to the left of the sorted pivot, and\n    elements in the second group appear to the right of the sorted pivot.\n    :param a: List subclass type; an object from a class that implements the List interface\n    :param start: int type; the index of the first element in the sublist that will be partitioned\n    :param end: int type; the index of the last element in the sublist that will be partitioned\n    """  # inserted
    l = start + 1
    r = end
    pivot = a.get(start)
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l = l + 1
        while r >= l and a.get(r) >= pivot:
            r = r - 1  
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else:  # inserted
            crossed = True
    a.set(start, a.get(r))
    a.set(r, pivot)
    return r

def _partition_r(a: List, start: int, end: int) -> int:
    """\n    helper method to _quick_sort_f(); partitions a sublist of the given list\n    using a random element in the sublist as pivot. The elements of the sublist\n    are arranged into two groups: the first group consists of elements\n    that are less than or equal to the pivot. The second group is\n    a group of elements that are greater than the pivot.  By the end of the\n    partitioning process, the pivot is placed in its correct, sorted order,\n    elements in the first group appear to the left of the sorted pivot, and\n    elements in the second group appear to the right of the sorted pivot.\n    :param a: List subclass type; an object from a class that implements the List interface\n    :param start: int type; the index of the first element in the sublist that will be partitioned\n    :param end: int type; the index of the last element in the sublist that will be partitioned\n    """  # inserted
    idx = random.randint(start, end)
    rand_ele = a.get(idx)
    a.set(idx, a.get(start))
    a.set(start, rand_ele)
    pivot = a.get(start)
    l = start + 1
    r = end
    crossed = False
    while not crossed:
        while l <= r and a.get(l) <= pivot:
            l = l + 1
        while r >= l and a.get(r) >= pivot:
            r = r - 1  
        if l < r:
            temp = a.get(l)
            a.set(l, a.get(r))
            a.set(r, temp)
        else: 
            crossed = True
    a.set(start, a.get(r))
    a.set(r, pivot)
    return r

def _quick_sort_f(a: List, start: int, end: int) -> None:
    """\n    helper method to quick_sort(); uses quick-sort with first-element pivot\n    to sort a sublist of the given list.\n    :param a: List subclass type; an object from a class that implements the List interface\n    :param start: int type; the index of the first element in the sublist\n    :param end: int type; the index of the last element in the sublist\n    """  # inserted
    if start < end:
        p = _partition_f(a, start, end)
        _quick_sort_f(a, start, p - 1)  
        _quick_sort_f(a, p + 1, end)    

def _quick_sort_r(a: List, start: int, end: int) -> None:
    """\n    helper method to quick_sort(); uses quick-sort with random-element pivot\n    to sort a sublist of the given list.\n    :param a: List subclass type; an object from a class that implements the List interface\n    :param start: int type; the index of the first element in the sublist\n    :param end: int type; the index of the last element in the sublist\n    """  # inserted
    if start < end:
        p = _partition_r(a, start, end)
        _quick_sort_r(a, start, p - 1)  
        _quick_sort_r(a, p + 1, end)  
def quick_sort(a: List, p: bool = True) -> None:
    """\n    sorts the given List using the quick sort algorithm.\n    :param a: List subclass type; an object from a class that\n    implements the List interface\n    :param p: boolean type; if True, the quick-sort algorithm uses a\n              randomly chosen element from a as pivot.\n              Otherwise, uses the first element as pivot.\n    """  # inserted
    if p:
        _quick_sort_r(a, 0, a.size() - 1)  
    else:  # inserted
        _quick_sort_f(a, 0, a.size() - 1)  