def solution(A):
    """Check if an array is a permutation.

    A permutation is a sequence containing each element from 1 to N once, and
    only once.

    Args:
        A (list): A non-empty list of N integers.

    Returns:
        int: 1 if the array is a permutation, 0 if it is not.

    Complexity:
        Time: O(N)
        Space: O(N)
    """

    N = len(A)
    if N == 0:
        return 0
    
    counter = [False] * N
    for val in A:
        if (val > N) or (val < 1):
            return 0

        if counter[val-1]:
            return 0
        else:
            counter[val-1] = True
    else:
        return 1
    
