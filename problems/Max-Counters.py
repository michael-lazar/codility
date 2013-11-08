def solution(N, A):

    max_counter = 0
    min_counter = 0
    counters = [0] * N

    for index in A:        
        if index == N+1:
            min_counter = max_counter
        else:
            counter = counters[index-1]
            if counter < min_counter:
                counter = min_counter
            counter += 1
            
            if counter > max_counter:
                max_counter = counter

            counters[index-1] = counter

    for i, counter in enumerate(counters):
        counters[i] = max(min_counter, counter)

    return counters
