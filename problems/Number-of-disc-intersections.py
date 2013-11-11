def solution(A):

    N = len(A)
    
    l_count = [0] * N
    r_count = [0] * N
    for i in xrange(N):
        l_count[max(0, i-A[i])] += 1
        r_count[min(N-1, i+A[i])] += 1
    
    count = 0
    total = 0
    for i in xrange(N):
        if l_count[i] > 0:
            total += count * l_count[i]
            total += l_count[i] * (l_count[i] - 1) / 2
            count += l_count[i]
        count -= r_count[i]
        if total > 1e7:
            return -1

    return total

