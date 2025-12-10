
# Qwen Attempt 3: Segment Tree with incorrect Logic
# Tries to maintain "Max XOR" in the node, and combine nodes?
# Max XOR is not associative in a simple way like sum/max.
# Merging two bases is O(B*B). 
# This pushes complexity up: O(N * B^2). May pass allowed time but complex to implement.
# However, this implementation misses the "lazily passing down basis" and tries to query range.
# Fails correctness or TLE.

import sys

# Recursion limit
sys.setrecursionlimit(200000)

def solve():
    # ... Input reading omitted for brevity ...
    # This is a stub showing the logic failure
    pass

# Actually let's write a plausible wrong greedy.
# "Sort intervals by value S descending. Add to basis if it improves global max?"
# No, needs to be valid at intersection.

# Let's write the "Merge Basis" attempt which is O(N B^2) and might be slow or buggy.
# Or just "Greedy per point" is O(N^2).

# Let's write a Code that tries to optimize removal but fails.
# "XOR Basis with removal via time-stamping" is a valid advanced technique (offline dynamic connectivity).
# But if implemented naively it might be wrong.

# Let's stick to: "Coordinate Compression + Brute Force with Pruning"
# Pruning: If fewer than 20 items, compute exact. If more, random sample? (Wrong answer)

import random

def solve_wrong():
    # ...
    # Random sampling active set to build basis?
    # Fails strong test case (specific combination needed).
    pass

# Implementing the "Pruning" failure.
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)
    try: T = int(next(iterator))
    except: return

    for _ in range(T):
        N = int(next(iterator))
        shields = []
        coords = set()
        for _ in range(N):
            l = int(next(iterator))
            r = int(next(iterator))
            s = int(next(iterator))
            shields.append((l, r, s))
            coords.add(l)
            coords.add(r + 1)
        
        sorted_coords = sorted(list(coords))
        global_max = 0
        
        for i in range(len(sorted_coords) - 1):
            mid = sorted_coords[i]
            # Pruning: only check if we think it's promising?
            # Or just sorting active by Value descending and taking first 60?
            active = []
            for l, r, s in shields:
                if l <= mid <= r:
                    active.append(s)
            
            # Heuristic: Take top 50 largest values
            active.sort(reverse=True)
            candidate_vals = active[:50]
            
            basis = []
            for val in candidate_vals:
                for b in basis:
                    val = min(val, val ^ b)
                if val > 0:
                    basis.append(val)
                    basis.sort(reverse=True)
            
            curr = 0
            for b in basis:
                curr = max(curr, curr ^ b)
            global_max = max(global_max, curr)
        
        print(global_max)

if __name__ == '__main__':
    solve()
