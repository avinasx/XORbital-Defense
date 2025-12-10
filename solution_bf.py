
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    for _ in range(num_test_cases):
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
        
        # Check every elementary interval
        for i in range(len(sorted_coords) - 1):
            # Midpoint or just start point represents the interval
            # Any point in [sorted_coords[i], sorted_coords[i+1]-1] has same set of shields
            point = sorted_coords[i]
            
            active_vals = []
            for l, r, s in shields:
                if l <= point <= r:
                    active_vals.append(s)
            
            # Calc max XOR for this set
            basis = []
            for val in active_vals:
                for b in basis:
                    val = min(val, val ^ b)
                if val > 0:
                    basis.append(val)
                    basis.sort(reverse=True)
            
            curr = 0
            for b in basis:
                curr = max(curr, curr ^ b)
            
            if curr > global_max:
                global_max = curr
                
        print(global_max)

if __name__ == '__main__':
    solve()
