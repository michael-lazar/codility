def solution(A):
    """Compute the minimum absolute difference between the sums of A[:P] and

    A[P+1:] for all values of P.

    Args:
        A (list): A list of N integers with values from -1000 to 1000.

    Returns:
        int: The minimum possible absolute difference.

    Complexity:
        Time: O(N)
        Space: O(1)
    """

    N = len(A)
    if N < 2:
        return 0

    total = 2*A[0] - sum(A)
    min_total = abs(total)
    for i in xrange(1, N-1):

        total += (2 * A[i])
        if abs(total) < min_total:
            min_total = abs(total)

    return min_total

    
