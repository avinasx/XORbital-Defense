
# Qwen Attempt 2: Sweep Line Optimization
# Logic: Use a heap to maintain active intervals.
# But "removing" from a Linear Basis is hard. 
# Attempt: Rebuild basis from heap at each step.
# Complexity: Each event, heap size ~N. Rebuild basis O(HeapSize * B).
# Total O(N * N * B). Still TLE on worst case (dense overlap).

import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)
    if not input_data: return
    
    try:
        T_cases = int(next(iterator))
    except: return

    for _ in range(T_cases):
        N = int(next(iterator))
        events = []
        for i in range(N):
            l = int(next(iterator))
            r = int(next(iterator))
            s = int(next(iterator))
            events.append((l, 1, s, i)) # 1 for start
            events.append((r + 1, -1, s, i)) # -1 for end
        
        events.sort()
        
        active_shields = set()
        global_max = 0
        
        # Iterate events
        for i in range(len(events)):
            x, type, s, idx = events[i]
            
            if type == 1:
                active_shields.add((s, idx))
            else:
                active_shields.remove((s, idx))
            
            # Don't process if next event is at same coordinate?
            if i + 1 < len(events) and events[i+1][0] == x:
                continue
                
            # Process active set
            # Rebuild basis from scratch
            basis = []
            for val, _ in active_shields:
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
