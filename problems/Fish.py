def solution(A, B):
    """Determine the number of fish that will not be eaten by larger fish.

    Fish are deemed alive if there are no larger fish that cross their path.
    Fish move in the following direction, denoted in vector B:
        (1) Fish k swims downstream if B[k] == 1
        (2) Fish k swims upstream if B[k] == 0

    Args:
        A (list): A vector in which A[k] denotes the kth fish's unique size.
        B (list): A vector in which B[k] denotes the kth fish's direction.

    Returns:
        int: The number of fish that have not been eaten after infinite time.

    Complexity:
        Time: O(N)
        Space: O(N)
    """

    N = len(A)
    
    downstream_stack = list()
    upstream_survivors = 0
    for i in xrange(0, N):
        if B[i] == 1:
            downstream_stack.append(A[i])
        else:
            while len(downstream_stack) > 0:
                if downstream_stack[-1] > A[i]:
                    break
                else:
                    downstream_stack.pop()
            else:
                upstream_survivors += 1

    total_survivors = len(downstream_stack) + upstream_survivors
    return total_survivors
