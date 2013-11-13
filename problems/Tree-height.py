def solution(T):
    height = search_tree(T, 0)
    return height
   
def search_tree(node, i):
    if node is None:
        return i - 1
    else:
        l_count = search_tree(node.l, i+1)
        r_count = search_tree(node.r, i+1)
        return max(l_count, r_count)
