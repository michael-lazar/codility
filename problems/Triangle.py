def solution(A):
    """Determine if a triangular triplet exists within a list of integers.

    A triangular triplet consists of three points P, Q, and R, where:
        (1) P + Q > R
        (2) Q + R > P
        (3) R + P > Q

    Args:
        A (list): A list of N integers.

    Returns:
        int: 1 if a triangular triplet exists, 0 if not.

    Complexity:
        Time: O(N*log(N))
        Space: O(N)
    """
    
    A = sorted(A)

    N = len(A)
    if N < 3:
        return 0

    for i in xrange(2, N):
        if A[i] < (A[i-1] + A[i-2]):
            return 1
    else:
        return 0

    

    

    

    
