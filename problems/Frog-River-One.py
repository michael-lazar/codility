def solution(X, A):
    """Find the earliest time that a frog can jump to position X.

    In order to reach X, a leaf must be present at every position from 1 to X.

    Args:
        X (int): The position that the frog must reach.
        A (list): A list of integers from 1 to X, where A[k] represents a leaf
            falling at minute k into position A[k].

    Returns:
        int: The number of minutes that the frog must wait.

    Complexity:
        Time: O(N)
        Space: O(X)
    """

    counter = [False] * X
    total = 0
    
    for i, val in enumerate(A):
        if (val < 1) or (val > X):
            raise ValueError
        
        if not counter[val-1]:
            counter[val-1] = True
            total += 1
            if total == X:
                return i
    else:
        return -1
