def solution(A):
    """Compute the maximum product of any triplet within a list.

    Args:
        A (list): A collection of N integers.

    Returns:
        int: The maximum pruduct that can be derived from A.
    
    Complexity:
        Time: O(N * log(N))
        Space: O(N)
    """

    if len(A) < 3:
        return 0
    
    A = sorted(A)

    product_A = A[0] * A[1] * A[-1]
    product_B = A[-1] * A[-2] * A[-3]
    max_product = max(product_A, product_B)

    return max_product

    
