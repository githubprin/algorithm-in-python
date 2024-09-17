def get_insert_idx(res, elem, cmp = lambda x, y: x if x > y else y):
    """
    Determines the appropriate index at which to insert an element into a sorted list to maintain the list's sorted order.

    Parameters:
    - res (list): A list of elements that is already sorted according to the comparison function 'cmp'.
    - elem (Any): The element to be inserted into the list.
    - cmp (callable, optional): A comparison function that takes two elements and returns the one that should come first in the sorted order. Defaults to a function that returns the greater of two elements.

    Returns:
    - int: The index at which 'elem' should be inserted into 'res' to maintain the sorted order.

    Detailed Explanation:
    The `get_insert_idx` function searches through the sorted list `res` to find the correct position for `elem`. It uses the comparison function `cmp` to determine the ordering between elements. The function ensures that after insertion, `res` remains sorted according to `cmp`.

    Example:
        res = [1, 3, 5, 7]
        elem = 4
        idx = get_insert_idx(res, elem, cmp=lambda x, y: x if x < y else y)
        res.insert(idx, elem)
        print(res)  # Output: [1, 3, 4, 5, 7]

    Visual Illustration:

        Before insertion:

        res: [1, 3, 5, 7]
                      ^
        Find position where elem=4 fits.

        After insertion:

        res: [1, 3, 4, 5, 7]
    """
    return 0

def sort3_insert(lst, cmp = lambda x, y: x if x > y else y):
    """
    Sorts a list of elements using the insertion sort algorithm.

    Parameters:
    - lst (list): The list of elements to be sorted.
    - cmp (callable, optional): A comparison function that takes two elements and returns the one that should come first. Defaults to a function that returns the greater of two elements (i.e., sorts in descending order).

    Returns:
    - list: A new list containing the sorted elements.

    Detailed Explanation:
    The `sort3_insert` function implements the insertion sort algorithm by building a new sorted list `res`. It iterates over each element in the input list `lst`, finds the appropriate index to insert the element into `res` using `get_insert_idx`, and inserts it. This process maintains the sorted order of `res`.

    Example:
        lst = [4, 2, 5, 1, 3]
        sorted_lst = sort3_insert(lst, cmp=lambda x, y: x if x < y else y)
        print(sorted_lst)  # Output: [1, 2, 3, 4, 5]

    Visual Illustration:

        Initial list: [4, 2, 5, 1, 3]

        Iteration 1:
        res = []
        Insert 4 into res:
        res = [4]

        Iteration 2:
        Insert 2 into res:
        res = [2, 4]

        Iteration 3:
        Insert 5 into res:
        res = [2, 4, 5]

        Iteration 4:
        Insert 1 into res:
        res = [1, 2, 4, 5]

        Iteration 5:
        Insert 3 into res:
        res = [1, 2, 3, 4, 5]
    """
    res = []
    for elem in lst:
        new_idx = get_insert_idx(res, elem, cmp=cmp)
        res.insert(new_idx, elem)
    return res

def merge_sort(lst, cmp = lambda x, y: x if x > y else y):
    """
    Sorts a list of elements using the merge sort algorithm.

    Parameters:
    - lst (list): The list of elements to be sorted.
    - cmp (callable, optional): A comparison function that takes two elements and returns the one that should come first. Defaults to a function that returns the greater of two elements (i.e., sorts in descending order).

    Returns:
    - list: A new list containing the sorted elements.

    Detailed Explanation:
    Merge sort is a divide-and-conquer algorithm that divides the input list into halves, recursively sorts each half, and then merges the sorted halves to produce the final sorted list.

    Steps:
    1. If the list has zero or one element, it is already sorted.
    2. Otherwise, divide the list into two halves.
    3. Recursively apply merge sort to each half.
    4. Merge the two sorted halves into a single sorted list using the `merge` function.

    Example:
        lst = [38, 27, 43, 3, 9, 82, 10]
        sorted_lst = merge_sort(lst, cmp=lambda x, y: x if x < y else y)
        print(sorted_lst)  # Output: [3, 9, 10, 27, 38, 43, 82]

    Visual Illustration:

        Splitting phase:

                     [38, 27, 43, 3, 9, 82, 10]
                              /              \
                   [38, 27, 43]            [3, 9, 82, 10]
                    /         \             /           \
                [38]       [27, 43]     [3, 9]       [82, 10]
                             /    \       /   \         /    \
                          [27]  [43]   [3]   [9]     [82]  [10]

        Merging phase:

              Merge [27, 43] and [38]       =>     [27, 38, 43]
              Merge [3, 9] and [10, 82]     =>     [3, 9, 10, 82]
        Combining [27, 38, 43] and [3, 9, 10, 82] results in:
            [3, 9, 10, 27, 38, 43, 82]
    """
    return lst

def merge(left, right, cmp = lambda x, y: x if x > y else y):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
    - left (list): The first sorted list.
    - right (list): The second sorted list.
    - cmp (callable, optional): A comparison function that takes two elements and returns the one that should come first. Defaults to a function that returns the greater of two elements.

    Returns:
    - list: A new list containing all elements from `left` and `right`, sorted according to `cmp`.

    Detailed Explanation:
    The `merge` function combines two sorted lists into one by repeatedly comparing the front elements of each list and moving the smaller (or larger, depending on `cmp`) into the result list.

    Example:
        left = [1, 4, 7]
        right = [2, 5, 6, 8]
        merged = merge(left, right, cmp=lambda x, y: x if x < y else y)
        print(merged)  # Output: [1, 2, 4, 5, 6, 7, 8]

    Visual Illustration:

        left:  [1, 4, 7]
        right: [2, 5, 6, 8]
        merged: []

        Steps:
        - Compare 1 and 2: append 1 to merged
        - Compare 4 and 2: append 2 to merged
        - Compare 4 and 5: append 4 to merged
        - Compare 7 and 5: append 5 to merged
        - Compare 7 and 6: append 6 to merged
        - Append remaining elements: 7 and 8
        Result: [1, 2, 4, 5, 6, 7, 8]
    """
    return left + right

def quick_sort(lst, cmp = lambda x, y: x if x > y else y):
    """
    Sorts a list of elements using the quick sort algorithm.

    Parameters:
    - lst (list): The list of elements to be sorted.
    - cmp (callable, optional): A comparison function that takes two elements and returns the one that should come first. Defaults to a function that returns the greater of two elements (i.e., sorts in descending order).

    Returns:
    - list: A new list containing the sorted elements.

    Detailed Explanation:
    Quick sort is a divide-and-conquer algorithm that selects a 'pivot' element and partitions the other elements into two sub-lists, according to whether they are less than or greater than the pivot. The sub-lists are then sorted recursively.

    Steps:
    1. Choose a pivot element from the list.
    2. Partition the list into two lists:
       - Elements less than the pivot.
       - Elements greater than the pivot.
    3. Recursively apply quick sort to the sub-lists.
    4. Combine the sorted sub-lists and pivot to produce the final sorted list.

    Example:
        lst = [10, 7, 8, 9, 1, 5]
        sorted_lst = quick_sort(lst, cmp=lambda x, y: x if x < y else y)
        print(sorted_lst)  # Output: [1, 5, 7, 8, 9, 10]

    Visual Illustration:

        Original list: [10, 7, 8, 9, 1, 5]
        Pivot: 10

        Partitioning:
        - Less than pivot: [7, 8, 9, 1, 5]
        - Greater than pivot: []

        Recursively sort [7, 8, 9, 1, 5]

        Pivot: 7
        Partitioning:
        - Less than pivot: [1, 5]
        - Greater than pivot: [8, 9]

        Recursively sort [1, 5] and [8, 9]

        Combine all to get the sorted list:
        [1, 5, 7, 8, 9, 10]
    """
    return lst

def tim_sort(lst, cmp = lambda x, y: x if x > y else y):
    """
    Sorts a list of elements using the TimSort algorithm.

    Parameters:
    - lst (list): The list of elements to be sorted.
    - cmp (callable, optional): A comparison function that takes two elements and returns the one that should come first. Defaults to a function that returns the greater of two elements (i.e., sorts in descending order).

    Returns:
    - list: A new list containing the sorted elements.

    Detailed Explanation:
    TimSort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on real-world data, which often contains runs of consecutive ordered elements.

    Key Concepts:
    - Runs: A sequence of consecutive elements that are already ordered.
    - Insertion Sort: Used on small runs because it's efficient for small datasets.
    - Merge: Merging the sorted runs to produce the final sorted list.

    Steps:
    1. Divide the list into small pieces called "runs" (default size is 32).
    2. Sort each run using insertion sort.
    3. Merge the sorted runs using a merge sort to produce the final sorted list.

    Example:
        lst = [5, 21, 7, 23, 19, 10, 12]
        sorted_lst = tim_sort(lst, cmp=lambda x, y: x if x < y else y)
        print(sorted_lst)  # Output: [5, 7, 10, 12, 19, 21, 23]

    Visual Illustration:

        Identifying runs:

        [5, 21] - increasing run
        [7, 23] - increasing run
        [19, 10, 12] - decreasing run (will be reversed)

        After sorting runs:

        [5, 21]
        [7, 23]
        [10, 12, 19]

        Merging runs:

        Merge [5, 21] and [7, 23] -> [5, 7, 21, 23]
        Merge result with [10, 12, 19] -> [5, 7, 10, 12, 19, 21, 23]
    """
    return lst
