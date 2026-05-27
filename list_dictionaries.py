"""
Miracle Python Training - Collections Module (Lists, Sets, Tuples, Dictionaries)
Employee Name: Geetha Gangabattula
Topic: Python Collections - Comprehensive Programs
Status: Completed
Date: 2026-05-27

This module demonstrates proper collection handling with:
- List operations and manipulations
- Set operations and comparisons
- Tuple creation and transformation
- Dictionary operations and conversions
- Best practices
- Comprehensive error handling
- Type hints and documentation
"""

from typing import List, Set, Tuple, Dict, Any, Union
from collections import Counter


# ============================================================================
# PROGRAM 1: SUM OF ELEMENTS IN A LIST
# ============================================================================

def sum_list_elements(lst: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the sum of all elements in a list.
    
    Args:
        lst (List[Union[int, float]]): List of numbers
    
    Returns:
        Union[int, float]: Sum of all elements
    
    Raises:
        TypeError: If list contains non-numeric values
        ValueError: If list is empty
    
    Example:
        >>> sum_list_elements([10, 20, 30, 40])
        100
    """
    if not lst:
        raise ValueError("❌ List cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("❌ All elements must be numeric")
    
    return sum(lst)


def demo_sum_of_elements() -> None:
    """Demonstrate sum of list elements."""
    print("\n" + "="*70)
    print("PROGRAM 1: SUM OF ELEMENTS IN A LIST")
    print("="*70)
    
    try:
        lst = [10, 20, 30, 40]
        result = sum_list_elements(lst)
        
        print(f"\nList: {lst}")
        print(f"✓ Sum: {result}")
    except (TypeError, ValueError) as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 2: LARGEST NUMBER IN THE LIST
# ============================================================================

def find_largest_number(lst: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the largest number in a list.
    
    Args:
        lst (List[Union[int, float]]): List of numbers
    
    Returns:
        Union[int, float]: Largest number
    
    Raises:
        ValueError: If list is empty
        TypeError: If list contains non-numeric values
    
    Example:
        >>> find_largest_number([12, 45, 67, 23, 89])
        89
    """
    if not lst:
        raise ValueError("❌ List cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("❌ All elements must be numeric")
    
    return max(lst)


def demo_largest_number() -> None:
    """Demonstrate finding largest number."""
    print("\n" + "="*70)
    print("PROGRAM 2: LARGEST NUMBER IN THE LIST")
    print("="*70)
    
    try:
        lst = [12, 45, 67, 23, 89]
        largest = find_largest_number(lst)
        
        print(f"\nList: {lst}")
        print(f"✓ Largest Number: {largest}")
    except (TypeError, ValueError) as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 3: REMOVING COMMON ELEMENTS
# ============================================================================

def remove_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Remove common elements from two lists (symmetric difference).
    
    Elements that appear in either list but not in both are returned.
    
    Args:
        list1 (List[Any]): First list
        list2 (List[Any]): Second list
    
    Returns:
        List[Any]: List of non-common elements
    
    Example:
        >>> remove_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7])
        [1, 2, 3, 6, 7]
    """
    result = []
    
    # Elements in list1 but not in list2
    for i in list1:
        if i not in list2:
            result.append(i)
    
    # Elements in list2 but not in list1
    for i in list2:
        if i not in list1:
            result.append(i)
    
    return sorted(result)  # Return sorted for consistency


def demo_remove_common_elements() -> None:
    """Demonstrate removing common elements."""
    print("\n" + "="*70)
    print("PROGRAM 3: REMOVING COMMON ELEMENTS")
    print("="*70)
    
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7]
    
    result = remove_common_elements(list1, list2)
    
    print(f"\nList 1: {list1}")
    print(f"List 2: {list2}")
    print(f"✓ After Removing Common Elements: {result}")
    print(f"  (Elements in one list but not both)")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 4: SECOND-SMALLEST NUMBER IN A LIST
# ============================================================================

def find_second_smallest(lst: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the second-smallest number in a list.
    
    Args:
        lst (List[Union[int, float]]): List of numbers
    
    Returns:
        Union[int, float]: Second smallest number
    
    Raises:
        ValueError: If list has less than 2 elements
        TypeError: If list contains non-numeric values
    
    Example:
        >>> find_second_smallest([12, 3, 45, 6, 7])
        6
    """
    if not lst:
        raise ValueError("❌ List cannot be empty")
    
    if len(lst) < 2:
        raise ValueError("❌ List must have at least 2 elements")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("❌ All elements must be numeric")
    
    sorted_lst = sorted(lst)
    return sorted_lst[1]


def demo_second_smallest() -> None:
    """Demonstrate finding second-smallest number."""
    print("\n" + "="*70)
    print("PROGRAM 4: SECOND-SMALLEST NUMBER IN A LIST")
    print("="*70)
    
    try:
        lst = [12, 3, 45, 6, 7]
        second_smallest = find_second_smallest(lst)
        
        print(f"\nList: {lst}")
        print(f"Sorted: {sorted(lst)}")
        print(f"✓ Second Smallest: {second_smallest}")
    except (TypeError, ValueError) as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 5: ELEMENTS IN ONE SET BUT NOT IN ANOTHER
# ============================================================================

def find_set_difference(set1: Set[Any], set2: Set[Any]) -> Tuple[Set[Any], Set[Any]]:
    """
    Find elements in one set but not in another.
    
    Args:
        set1 (Set[Any]): First set
        set2 (Set[Any]): Second set
    
    Returns:
        Tuple[Set[Any], Set[Any]]: (elements in set1 but not set2, vice versa)
    
    Example:
        >>> find_set_difference({1, 2, 3, 4, 5}, {4, 5, 6, 7})
        ({1, 2, 3}, {6, 7})
    """
    return set1 - set2, set2 - set1


def demo_set_difference() -> None:
    """Demonstrate set difference operations."""
    print("\n" + "="*70)
    print("PROGRAM 5: ELEMENTS IN ONE SET BUT NOT IN ANOTHER")
    print("="*70)
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    
    diff1, diff2 = find_set_difference(set1, set2)
    
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"✓ Elements in Set 1 but not Set 2: {diff1}")
    print(f"✓ Elements in Set 2 but not Set 1: {diff2}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 6: MISSING NUMBERS BETWEEN TWO SETS
# ============================================================================

def find_missing_numbers(set1: Set[int], set2: Set[int]) -> Tuple[Set[int], Set[int]]:
    """
    Find missing numbers between two sets.
    
    Args:
        set1 (Set[int]): First set of numbers
        set2 (Set[int]): Second set of numbers
    
    Returns:
        Tuple[Set[int], Set[int]]: (missing in set2, missing in set1)
    
    Example:
        >>> find_missing_numbers({1, 2, 3, 4, 5}, {4, 5, 6, 7})
        ({1, 2, 3}, {6, 7})
    """
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    
    return missing_in_set2, missing_in_set1


def demo_missing_numbers() -> None:
    """Demonstrate finding missing numbers."""
    print("\n" + "="*70)
    print("PROGRAM 6: MISSING NUMBERS BETWEEN TWO SETS")
    print("="*70)
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    
    missing_in_set2, missing_in_set1 = find_missing_numbers(set1, set2)
    
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"✓ Missing in Set 2: {missing_in_set2}")
    print(f"✓ Missing in Set 1: {missing_in_set1}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 7: PAIRS WHOSE SUM EQUALS GIVEN VALUE
# ============================================================================

def find_pairs_with_sum(lst: List[Union[int, float]], 
                       target: Union[int, float]) -> List[Tuple[Union[int, float], Union[int, float]]]:
    """
    Find all pairs of numbers whose sum equals the target value.
    
    Args:
        lst (List[Union[int, float]]): List of numbers
        target (Union[int, float]): Target sum
    
    Returns:
        List[Tuple[Union[int, float], Union[int, float]]]: List of pairs
    
    Example:
        >>> find_pairs_with_sum([1, 2, 3, 4, 5, 6], 7)
        [(1, 6), (2, 5), (3, 4)]
    """
    pairs = []
    
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    
    return pairs


def demo_pairs_with_sum() -> None:
    """Demonstrate finding pairs with target sum."""
    print("\n" + "="*70)
    print("PROGRAM 7: PAIRS WHOSE SUM IS EQUAL TO GIVEN VALUE")
    print("="*70)
    
    lst = [1, 2, 3, 4, 5, 6]
    target = 7
    
    pairs = find_pairs_with_sum(lst, target)
    
    print(f"\nList: {lst}")
    print(f"Target Sum: {target}")
    print(f"✓ Pairs:")
    
    for pair in pairs:
        print(f"  {pair[0]} + {pair[1]} = {target}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 8: TWO NUMBERS WITH MAXIMUM PRODUCT
# ============================================================================

def find_max_product_pair(lst: List[Union[int, float]]) -> Tuple[Tuple[Union[int, float], Union[int, float]], Union[int, float]]:
    """
    Find two numbers whose product is maximum.
    
    Args:
        lst (List[Union[int, float]]): List of numbers
    
    Returns:
        Tuple: ((num1, num2), product)
    
    Raises:
        ValueError: If list has less than 2 elements
    
    Example:
        >>> find_max_product_pair([1, 5, 10, 2, 8])
        ((10, 8), 80)
    """
    if len(lst) < 2:
        raise ValueError("❌ List must have at least 2 elements")
    
    sorted_lst = sorted(lst, reverse=True)
    max_pair = (sorted_lst[0], sorted_lst[1])
    product = max_pair[0] * max_pair[1]
    
    return max_pair, product


def demo_max_product_pair() -> None:
    """Demonstrate finding maximum product pair."""
    print("\n" + "="*70)
    print("PROGRAM 8: TWO NUMBERS WITH MAXIMUM PRODUCT")
    print("="*70)
    
    try:
        lst = [1, 5, 10, 2, 8]
        pair, product = find_max_product_pair(lst)
        
        print(f"\nList: {lst}")
        print(f"Sorted (descending): {sorted(lst, reverse=True)}")
        print(f"✓ Maximum Product Pair: {pair}")
        print(f"✓ Product: {pair[0]} × {pair[1]} = {product}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 9: MAXIMUM AND MINIMUM VALUES IN A SET
# ============================================================================

def find_set_extremes(s: Set[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Find maximum and minimum values in a set.
    
    Args:
        s (Set[Union[int, float]]): Set of numbers
    
    Returns:
        Tuple[Union[int, float], Union[int, float]]: (maximum, minimum)
    
    Raises:
        ValueError: If set is empty
    
    Example:
        >>> find_set_extremes({10, 20, 30, 40, 50})
        (50, 10)
    """
    if not s:
        raise ValueError("❌ Set cannot be empty")
    
    return max(s), min(s)


def demo_set_extremes() -> None:
    """Demonstrate finding set extremes."""
    print("\n" + "="*70)
    print("PROGRAM 9: MAXIMUM AND MINIMUM VALUES IN A SET")
    print("="*70)
    
    try:
        s = {10, 20, 30, 40, 50}
        maximum, minimum = find_set_extremes(s)
        
        print(f"\nSet: {s}")
        print(f"✓ Maximum: {maximum}")
        print(f"✓ Minimum: {minimum}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 10: REMOVE AN ITEM FROM A SET
# ============================================================================

def remove_from_set(s: Set[Any], item: Any) -> Set[Any]:
    """
    Remove an item from a set safely.
    
    Args:
        s (Set[Any]): Original set
        item (Any): Item to remove
    
    Returns:
        Set[Any]: Set after removal
    
    Note:
        - discard(): No error if item not present
        - remove(): Raises KeyError if item not present
    
    Example:
        >>> remove_from_set({1, 2, 3, 4, 5}, 3)
        {1, 2, 4, 5}
    """
    s.discard(item)  # Safe removal (no error if not found)
    return s


def demo_remove_from_set() -> None:
    """Demonstrate removing item from set."""
    print("\n" + "="*70)
    print("PROGRAM 10: REMOVE AN ITEM FROM A SET")
    print("="*70)
    
    s = {1, 2, 3, 4, 5}
    item_to_remove = 3
    
    print(f"\nOriginal Set: {s}")
    print(f"Removing: {item_to_remove}")
    
    result = remove_from_set(s.copy(), item_to_remove)
    
    print(f"✓ After Removal: {result}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 11: TUPLE WITH DIFFERENT DATA TYPES
# ============================================================================

def create_mixed_tuple(name: str, age: int, score: float, 
                      active: bool) -> Tuple[str, int, float, bool]:
    """
    Create a tuple containing different data types.
    
    Args:
        name (str): Name (string)
        age (int): Age (integer)
        score (float): Score (float)
        active (bool): Active status (boolean)
    
    Returns:
        Tuple[str, int, float, bool]: Mixed data type tuple
    
    Example:
        >>> create_mixed_tuple("Varshitha", 21, 95.5, True)
        ('Varshitha', 21, 95.5, True)
    """
    return (name, age, score, active)


def demo_mixed_tuple() -> None:
    """Demonstrate tuple with different data types."""
    print("\n" + "="*70)
    print("PROGRAM 11: TUPLE WITH DIFFERENT DATA TYPES")
    print("="*70)
    
    t = create_mixed_tuple("Varshitha", 21, 95.5, True)
    
    print(f"\n✓ Tuple: {t}")
    print(f"  Type: {type(t)}")
    print(f"  Data Types:")
    for i, item in enumerate(t):
        print(f"    Index {i}: {item} ({type(item).__name__})")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 12: UNPACK TUPLE INTO VARIABLES
# ============================================================================

def unpack_tuple(t: Tuple[Any, ...]) -> List[Any]:
    """
    Unpack a tuple into variables and return as list.
    
    Args:
        t (Tuple[Any, ...]): Tuple to unpack
    
    Returns:
        List[Any]: List of unpacked values
    
    Example:
        >>> unpack_tuple(("Apple", "Banana", "Mango"))
        ['Apple', 'Banana', 'Mango']
    """
    return list(t)


def demo_unpack_tuple() -> None:
    """Demonstrate unpacking tuple into variables."""
    print("\n" + "="*70)
    print("PROGRAM 12: UNPACK TUPLE INTO VARIABLES")
    print("="*70)
    
    t = ("Apple", "Banana", "Mango")
    a, b, c = t
    
    print(f"\nOriginal Tuple: {t}")
    print(f"✓ Unpacked Values:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  c = {c}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 13: FIND REPEATED ITEMS IN A TUPLE
# ============================================================================

def find_repeated_items(t: Tuple[Any, ...]) -> List[Any]:
    """
    Find repeated items in a tuple.
    
    Args:
        t (Tuple[Any, ...]): Tuple to check
    
    Returns:
        List[Any]: List of repeated items
    
    Example:
        >>> find_repeated_items((1, 2, 3, 2, 4, 5, 1))
        [1, 2]
    """
    repeated = []
    
    for item in set(t):
        if t.count(item) > 1:
            repeated.append(item)
    
    return sorted(repeated)


def demo_repeated_items() -> None:
    """Demonstrate finding repeated items."""
    print("\n" + "="*70)
    print("PROGRAM 13: FIND REPEATED ITEMS IN A TUPLE")
    print("="*70)
    
    t = (1, 2, 3, 2, 4, 5, 1)
    repeated = find_repeated_items(t)
    
    print(f"\nTuple: {t}")
    print(f"✓ Repeated Items:")
    
    for item in repeated:
        count = t.count(item)
        print(f"  {item} appears {count} times")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 14: REVERSE A TUPLE
# ============================================================================

def reverse_tuple(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Reverse a tuple.
    
    Args:
        t (Tuple[Any, ...]): Tuple to reverse
    
    Returns:
        Tuple[Any, ...]: Reversed tuple
    
    Example:
        >>> reverse_tuple((1, 2, 3, 4, 5))
        (5, 4, 3, 2, 1)
    """
    return t[::-1]


def demo_reverse_tuple() -> None:
    """Demonstrate reversing a tuple."""
    print("\n" + "="*70)
    print("PROGRAM 14: REVERSE A TUPLE")
    print("="*70)
    
    t = (1, 2, 3, 4, 5)
    reversed_t = reverse_tuple(t)
    
    print(f"\nOriginal Tuple: {t}")
    print(f"✓ Reversed Tuple: {reversed_t}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 15: REPLACE LAST VALUE IN TUPLES
# ============================================================================

def replace_last_value_in_tuples(lst: List[Tuple[Any, ...]], 
                                new_value: Any) -> List[Tuple[Any, ...]]:
    """
    Replace the last value in each tuple of a list.
    
    Args:
        lst (List[Tuple[Any, ...]]): List of tuples
        new_value (Any): New value for last position
    
    Returns:
        List[Tuple[Any, ...]]: List with replaced values
    
    Example:
        >>> replace_last_value_in_tuples([(10, 20, 40), (40, 50, 60)], 100)
        [(10, 20, 100), (40, 50, 100)]
    """
    return [t[:-1] + (new_value,) for t in lst]


def demo_replace_last_value() -> None:
    """Demonstrate replacing last value in tuples."""
    print("\n" + "="*70)
    print("PROGRAM 15: REPLACE LAST VALUE IN TUPLES")
    print("="*70)
    
    lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    new_value = 100
    
    result = replace_last_value_in_tuples(lst, new_value)
    
    print(f"\nOriginal List: {lst}")
    print(f"New Value: {new_value}")
    print(f"✓ After Replacing Last Value: {result}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 16: CONVERT TUPLE INTO INTEGER
# ============================================================================

def convert_tuple_to_integer(t: Tuple[int, ...]) -> int:
    """
    Convert tuple of digits into a single integer.
    
    Args:
        t (Tuple[int, ...]): Tuple of single digits
    
    Returns:
        int: Combined integer
    
    Raises:
        ValueError: If tuple is empty
        TypeError: If tuple contains non-digits
    
    Example:
        >>> convert_tuple_to_integer((1, 2, 3))
        123
    """
    if not t:
        raise ValueError("❌ Tuple cannot be empty")
    
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in t):
        raise TypeError("❌ All elements must be digits (0-9)")
    
    num = int("".join(map(str, t)))
    return num


def demo_convert_tuple_to_int() -> None:
    """Demonstrate converting tuple to integer."""
    print("\n" + "="*70)
    print("PROGRAM 16: CONVERT TUPLE INTO INTEGER")
    print("="*70)
    
    try:
        t = (1, 2, 3)
        num = convert_tuple_to_integer(t)
        
        print(f"\nTuple: {t}")
        print(f"✓ Converted Integer: {num}")
        print(f"  Type: {type(num).__name__}")
    except (ValueError, TypeError) as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 17: SUM OF ELEMENTS OF EACH TUPLE
# ============================================================================

def sum_elements_each_tuple(lst: List[Tuple[Union[int, float], ...]]) -> List[Union[int, float]]:
    """
    Calculate sum of elements in each tuple.
    
    Args:
        lst (List[Tuple[Union[int, float], ...]]): List of numeric tuples
    
    Returns:
        List[Union[int, float]]: List of sums
    
    Example:
        >>> sum_elements_each_tuple([(1, 2), (2, 3), (3, 4)])
        [3, 5, 7]
    """
    return [sum(t) for t in lst]


def demo_sum_each_tuple() -> None:
    """Demonstrate summing each tuple's elements."""
    print("\n" + "="*70)
    print("PROGRAM 17: SUM OF ELEMENTS OF EACH TUPLE")
    print("="*70)
    
    lst = [(1, 2), (2, 3), (3, 4)]
    result = sum_elements_each_tuple(lst)
    
    print(f"\nList of Tuples: {lst}")
    print(f"✓ Sum of Each Tuple: {result}")
    
    for i, t in enumerate(lst):
        print(f"  {t} → sum = {result[i]}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 18: DICTIONARY WITH SQUARES
# ============================================================================

def create_squares_dict(n: int) -> Dict[int, int]:
    """
    Create a dictionary with numbers and their squares.
    
    Args:
        n (int): Range (1 to n)
    
    Returns:
        Dict[int, int]: Dictionary with {number: square}
    
    Raises:
        ValueError: If n is less than 1
    
    Example:
        >>> create_squares_dict(5)
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    if n < 1:
        raise ValueError("❌ n must be at least 1")
    
    return {i: i * i for i in range(1, n + 1)}


def demo_squares_dict() -> None:
    """Demonstrate dictionary with squares."""
    print("\n" + "="*70)
    print("PROGRAM 18: DICTIONARY WITH SQUARES")
    print("="*70)
    
    try:
        d = create_squares_dict(10)
        
        print(f"\n✓ Dictionary (Numbers and Squares):")
        print(f"  {d}")
        
        print(f"\nDetailed View:")
        for num, square in d.items():
            print(f"  {num}² = {square}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 19: COMBINE TWO DICTIONARIES
# ============================================================================

def combine_dictionaries(d1: Dict[Any, int], d2: Dict[Any, int]) -> Dict[Any, int]:
    """
    Combine two dictionaries by adding values for same keys.
    
    Args:
        d1 (Dict[Any, int]): First dictionary
        d2 (Dict[Any, int]): Second dictionary
    
    Returns:
        Dict[Any, int]: Combined dictionary with summed values
    
    Example:
        >>> combine_dictionaries({'a': 100, 'b': 200}, {'a': 300, 'b': 200, 'd': 400})
        Counter({'a': 400, 'b': 400, 'd': 400})
    """
    return Counter(d1) + Counter(d2)


def demo_combine_dicts() -> None:
    """Demonstrate combining dictionaries."""
    print("\n" + "="*70)
    print("PROGRAM 19: COMBINE TWO DICTIONARIES")
    print("="*70)
    
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    
    result = combine_dictionaries(d1, d2)
    
    print(f"\nDictionary 1: {d1}")
    print(f"Dictionary 2: {d2}")
    print(f"✓ Combined Dictionary: {dict(result)}")
    
    print(f"\nDetails:")
    for key, value in result.items():
        d1_val = d1.get(key, 0)
        d2_val = d2.get(key, 0)
        print(f"  '{key}': {d1_val} + {d2_val} = {value}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 20: CONVERT LISTS TO NESTED DICTIONARY
# ============================================================================

def create_nested_dict(ids: List[str], names: List[str], 
                       marks: List[int]) -> List[Dict[str, Dict[str, int]]]:
    """
    Convert lists into nested dictionary structure.
    
    Args:
        ids (List[str]): List of student IDs
        names (List[str]): List of student names
        marks (List[int]): List of student marks
    
    Returns:
        List[Dict[str, Dict[str, int]]]: Nested dictionary
    
    Raises:
        ValueError: If lists have different lengths
    
    Example:
        >>> create_nested_dict(['S001', 'S002'], ['Adina', 'Leyton'], [85, 98])
        [{'S001': {'Adina': 85}}, {'S002': {'Leyton': 98}}]
    """
    if not (len(ids) == len(names) == len(marks)):
        raise ValueError("❌ All lists must have same length")
    
    result = []
    
    for i in range(len(ids)):
        nested = {ids[i]: {names[i]: marks[i]}}
        result.append(nested)
    
    return result


def demo_nested_dict() -> None:
    """Demonstrate converting lists to nested dictionary."""
    print("\n" + "="*70)
    print("PROGRAM 20: CONVERT LISTS TO NESTED DICTIONARY")
    print("="*70)
    
    try:
        ids = ['S001', 'S002', 'S003', 'S004']
        names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
        marks = [85, 98, 89, 92]
        
        result = create_nested_dict(ids, names, marks)
        
        print(f"\nStudent IDs: {ids}")
        print(f"Names: {names}")
        print(f"Marks: {marks}")
        
        print(f"\n✓ Nested Dictionary Structure:")
        for item in result:
            print(f"  {item}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 21: CONVERT DICTIONARY INTO LIST OF LISTS
# ============================================================================

def dict_to_list_of_lists(d: Dict[Any, Any]) -> List[List[Any]]:
    """
    Convert dictionary into list of [key, value] pairs.
    
    Args:
        d (Dict[Any, Any]): Dictionary to convert
    
    Returns:
        List[List[Any]]: List of [key, value] pairs
    
    Example:
        >>> dict_to_list_of_lists({1: 'red', 2: 'green'})
        [[1, 'red'], [2, 'green']]
    """
    return [[k, v] for k, v in d.items()]


def demo_dict_to_list_of_lists() -> None:
    """Demonstrate converting dictionary to list of lists."""
    print("\n" + "="*70)
    print("PROGRAM 21: CONVERT DICTIONARY INTO LIST OF LISTS")
    print("="*70)
    
    d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
    result = dict_to_list_of_lists(d)
    
    print(f"\nOriginal Dictionary: {d}")
    print(f"✓ List of Lists:")
    print(f"  {result}")
    
    print(f"\nDetailed View:")
    for key, value in result:
        print(f"  [{key}, '{value}']")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 22: GET KEY, VALUE AND ITEM IN DICTIONARY
# ============================================================================

def get_dict_components(d: Dict[Any, Any]) -> Tuple[Any, Any, Any]:
    """
    Get keys, values, and items from dictionary.
    
    Args:
        d (Dict[Any, Any]): Dictionary
    
    Returns:
        Tuple: (dict_keys, dict_values, dict_items)
    
    Example:
        >>> get_dict_components({'a': 10, 'b': 20})
        (dict_keys(['a', 'b']), dict_values([10, 20]), dict_items([('a', 10), ('b', 20)]))
    """
    return d.keys(), d.values(), d.items()


def demo_dict_components() -> None:
    """Demonstrate getting dictionary components."""
    print("\n" + "="*70)
    print("PROGRAM 22: GET KEY, VALUE AND ITEM IN DICTIONARY")
    print("="*70)
    
    d = {'a': 10, 'b': 20, 'c': 30}
    keys, values, items = get_dict_components(d)
    
    print(f"\nDictionary: {d}")
    print(f"\n✓ Keys: {list(keys)}")
    print(f"✓ Values: {list(values)}")
    print(f"✓ Items: {list(items)}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 23: MAXIMUM AND MINIMUM VALUES IN DICTIONARY
# ============================================================================

def find_dict_extremes(d: Dict[Any, Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Find maximum and minimum values in dictionary.
    
    Args:
        d (Dict[Any, Union[int, float]]): Dictionary with numeric values
    
    Returns:
        Tuple[Union[int, float], Union[int, float]]: (max_value, min_value)
    
    Raises:
        ValueError: If dictionary is empty
    
    Example:
        >>> find_dict_extremes({'a': 10, 'b': 50, 'c': 5})
        (50, 5)
    """
    if not d:
        raise ValueError("❌ Dictionary cannot be empty")
    
    return max(d.values()), min(d.values())


def demo_dict_extremes() -> None:
    """Demonstrate finding dictionary extremes."""
    print("\n" + "="*70)
    print("PROGRAM 23: MAXIMUM AND MINIMUM VALUES IN DICTIONARY")
    print("="*70)
    
    try:
        d = {'a': 10, 'b': 50, 'c': 5}
        maximum, minimum = find_dict_extremes(d)
        
        print(f"\nDictionary: {d}")
        print(f"✓ Maximum Value: {maximum}")
        print(f"✓ Minimum Value: {minimum}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def display_menu() -> None:
    """Display menu of all programs."""
    menu = """
╔════════════════════════════════════════════════════════════╗
║   MIRACLE PYTHON TRAINING - COLLECTIONS MODULE (23 PROGS)  ║
║              Employee: Geetha Gangabattula                  ║
║                  Company: Miracle                           ║
╚════════════════════════════════════════════════════════════╝

SELECT A PROGRAM TO RUN:
 1. Sum of Elements in a List
 2. Largest Number in the List
 3. Removing Common Elements
 4. Second-Smallest Number
 5. Elements in One Set But Not Another
 6. Missing Numbers Between Sets
 7. Pairs Whose Sum Equals Target
 8. Two Numbers with Maximum Product
 9. Maximum and Minimum in Set
10. Remove Item from Set
11. Tuple with Different Data Types
12. Unpack Tuple into Variables
13. Find Repeated Items in Tuple
14. Reverse a Tuple
15. Replace Last Value in Tuples
16. Convert Tuple into Integer
17. Sum of Elements in Each Tuple
18. Dictionary with Squares
19. Combine Two Dictionaries
20. Convert Lists to Nested Dictionary
21. Convert Dictionary to List of Lists
22. Get Key, Value and Item in Dictionary
23. Maximum and Minimum Values in Dictionary
 0. Exit

"""
    print(menu)


def main() -> None:
    """Main execution function."""
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-23): ").strip()
            
            programs = {
                "1": demo_sum_of_elements,
                "2": demo_largest_number,
                "3": demo_remove_common_elements,
                "4": demo_second_smallest,
                "5": demo_set_difference,
                "6": demo_missing_numbers,
                "7": demo_pairs_with_sum,
                "8": demo_max_product_pair,
                "9": demo_set_extremes,
                "10": demo_remove_from_set,
                "11": demo_mixed_tuple,
                "12": demo_unpack_tuple,
                "13": demo_repeated_items,
                "14": demo_reverse_tuple,
                "15": demo_replace_last_value,
                "16": demo_convert_tuple_to_int,
                "17": demo_sum_each_tuple,
                "18": demo_squares_dict,
                "19": demo_combine_dicts,
                "20": demo_nested_dict,
                "21": demo_dict_to_list_of_lists,
                "22": demo_dict_components,
                "23": demo_dict_extremes,
            }
            
            if choice == "0":
                print("\n" + "="*70)
                print("✓ Thank you for using Miracle Python Training!")
                print("Employee: Geetha Gangabattula")
                print("Company: Miracle")
                print("="*70 + "\n")
                break
            
            if choice in programs:
                programs[choice]()
                input("Press Enter to continue...")
            else:
                print("\n❌ Invalid choice! Please select a valid program number.\n")
                input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}\n")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
