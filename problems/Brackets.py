def solution(S):
    """Check that a string is properly nested.

    A string is considered properly nested if one of the following is true:
        (1) S is empty
        (2) S has the form "(U)" or "[U]" or "{U}" where U is properly nested
        (3) S has the form "VW" where V and W are properly nested

    Args:
        S (str): An N character long string.

    Returns:
        int: 1 if S is properly nested, 0 if it is not.

    Complexity:
        Time: O(N)
        Space: O(N)
    """

    lookup = {'(':')', '{':'}', '[':']'}

    stack = list()
    for char in S:
        if char in lookup.keys():
            stack.append(char)
        else:
            if len(stack) < 1:
                return 0
            
            if lookup[stack[-1]] != char:
                return 0
            else:
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0
        
    
    
