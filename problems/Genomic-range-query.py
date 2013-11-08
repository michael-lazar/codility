def solution(S, P, Q):

    lookup = {'A':0, 'C':1, 'G':2, 'T':3}
    
    N = len(S)
    M = len(P)

    S = map(lookup.get, S)

    recent = [[-1] for _ in xrange(4)]
    for i, val in enumerate(S):
        for nucleotide in xrange(4):
            if nucleotide == val:
                recent[nucleotide].append(i)
            else:
                recent[nucleotide].append(recent[nucleotide][-1])

    A = []
    for start, end in zip(P,Q):       
        nucleotide = min(i for i in xrange(4) if recent[i][end+1] >= start)
        A.append(nucleotide + 1)

    return A

if __name__ == '__main__':

    result = solution('GACACCATA', [0, 0, 4, 7], [7, 2, 5, 7])
    print result
    
    
