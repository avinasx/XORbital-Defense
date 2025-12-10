
# Qwen Attempt 1: Brute Force approach
# Logic: Iterate through all coordinates x? No, x up to 10^9.
# Maybe iterate through elementary intervals but rebuild basis every time.
# Complexity: O(N^2 * B). TLE for N=50000.

import sys

def solve():
    # Read strict format
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)
    try:
        T = int(next(iterator))
    except StopIteration: return

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
        
        # This loop is O(N) because len(sorted_coords) <= 2N
        for i in range(len(sorted_coords) - 1):
            mid = sorted_coords[i]
            # This inner loop is O(N)
            active = []
            for l, r, s in shields:
                if l <= mid <= r:
                    active.append(s)
            
            # Basis construction O(N * 20)
            basis = []
            for val in active:
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
