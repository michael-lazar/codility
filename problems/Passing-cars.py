def solution(A):
    """Count the number of pairs of cars that pass each other. 

    Each element in A[k] represents a car at position k moving in direction:
        (1) right-bound if A[k] = 0
        (2) left-bound if A[k] = 1

    Args:
        A (list): A list of cars at positions k moving in directions A[k].

    Returns:
        int: The total pairs of passing cars. If the number exceeds 1e9,
            returns -1.

    Complexity:
        Time: O(N)
        Space: O(1)
    """

    n_pairs = 0
    right_bound = 0

    for direction in A:
        if n_pairs > 1e9:
            return -1
        
        if direction == 0:
            right_bound += 1
        else:
            n_pairs += right_bound

    return n_pairs
