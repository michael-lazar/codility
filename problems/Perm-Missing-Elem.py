def solution(A):
    """Find and return the missing element in a list.

    Args:
        A (list): List of N unique integers with values between 1 and (N+1).

    Returns:
        int: Value of the missing element.

    Complexity:
        Time: O(N)
        Space: O(1)
    """

    N = len(A)

    expected_sum = ((N+1)*(N+2))/2
    missing_value = expected_sum - sum(A)
    
    return missing_value





