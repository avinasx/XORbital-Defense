
import sys

# Increase recursion depth for deep segment trees
sys.setrecursionlimit(200000)

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    for _ in range(num_test_cases):
        try:
            N = int(next(iterator))
        except StopIteration:
            break
            
        shields = []
        coords = set()
        
        for _ in range(N):
            l = int(next(iterator))
            r = int(next(iterator))
            s = int(next(iterator))
            shields.append((l, r, s))
            coords.add(l)
            coords.add(r + 1)
            
        # Coordinate Compression
        sorted_coords = sorted(list(coords))
        rank = {val: i for i, val in enumerate(sorted_coords)}
        M = len(sorted_coords) - 1  # Number of elementary intervals
        
        # Segment Tree range [0, M-1]
        # tree[node] holds list of weights covering this range fully
        # Size 4*M is safe
        tree = [[] for _ in range(4 * M)]
        
        def update(node, start, end, idx_l, idx_r, val):
            if idx_l > end or idx_r < start:
                return
            if idx_l <= start and end <= idx_r:
                tree[node].append(val)
                return
            mid = (start + end) // 2
            update(2 * node, start, mid, idx_l, idx_r, val)
            update(2 * node + 1, mid + 1, end, idx_l, idx_r, val)

        for l, r, s in shields:
            # Map [l, r] to [rank[l], rank[r+1] - 1]
            # Because elementary interval i corresponds to [sorted_coords[i], sorted_coords[i+1]-1]
            idx_l = rank[l]
            idx_r = rank[r + 1] - 1
            if idx_l <= idx_r:
                update(1, 0, M - 1, idx_l, idx_r, s)
        
        max_xor_global = 0
        
        # Linear Basis logic
        # We represent basis as a list of numbers.
        # Since max val < 2^20, basis size <= 20.
        
        def insert_into_basis(basis, val):
            for b_val in basis:
                val = min(val, val ^ b_val)
            if val > 0:
                basis.append(val)
                basis.sort(reverse=True) # Keeping it sorted helps? Not strictly needed but clean.
                return True
            return False

        def get_max(basis):
            res = 0
            for b in basis:
                res = max(res, res ^ b)
            return res

        # DFS
        # We pass a COPY of the basis down.
        # Since basis is small (<=20 ints), copy is cheap.
        
        def dfs(node, start, end, current_basis):
            nonlocal max_xor_global
            
            # Add current node's values to basis
            # Optimization: Just extend and re-reduce?
            # Or insert one by one.
            # Copy basis first
            new_basis = list(current_basis)
            
            for val in tree[node]:
                # Insert val into new_basis
                # Inlining logic for speed
                x = val
                for b in new_basis:
                    x = min(x, x ^ b)
                if x > 0:
                    new_basis.append(x)
                    new_basis.sort(reverse=True)
            
            if start == end:
                # Leaf
                current_max = 0
                for b in new_basis:
                    current_max = max(current_max, current_max ^ b)
                if current_max > max_xor_global:
                    max_xor_global = current_max
                return

            mid = (start + end) // 2
            dfs(2 * node, start, mid, new_basis)
            dfs(2 * node + 1, mid + 1, end, new_basis)

        if M > 0:
            dfs(1, 0, M - 1, [])
        
        print(max_xor_global)

if __name__ == '__main__':
    solve()
