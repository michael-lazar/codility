def solution(X, Y, D):
    """Return the minimum number of jumps that a frog needs to make to get

    from position X to a position equal or greater than Y.

    Args:
        X (int): Starting position of frog.
        Y (int): Ending position of frog.
        D (int): Distance that the frog can jump.

    Returns:
        int: The minimum number of jumps needed.

    Complexity:
        Time: O(1)
        Space: O(1)
    """
    
    X, Y, D = int(X), int(Y), int(D)

    n_jumps, remainder = divmod(Y-X, D)
    if remainder != 0:
        n_jumps += 1

    return n_jumps
