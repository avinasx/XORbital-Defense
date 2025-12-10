# Solution: Cosmic Shields

## Analysis
The problem asks for the maximum XOR sum of any subset of active "shields" at any point $X$.
The set of active shields changes only at points $L_i$ and $R_i + 1$.
The values $L_i, R_i$ can be up to $10^9$, so we must use **Coordinate Compression**.

Let the sorted unique coordinates be $x_1, x_2, \dots, x_M$. These define $M-1$ elementary intervals $[x_j, x_{j+1}-1]$. Within each elementary interval, the set of active shields is constant.
We want to find:
$$ \max_{j} (\text{MaxXORSubset}(\text{Shields Active at } j)) $$

## Algorithm
1. **Coordinate Compression**: Collect all $L_i$ and $R_i+1$. Sort them to get elementary intervals.
2. **Segment Tree**: Build a Segment Tree over the elementary intervals.
   - Each shield $[L_i, R_i]$ covers a contiguous range of elementary intervals.
   - We efficiently add the shield's value $S_i$ to $O(\log M)$ nodes in the Segment Tree.
3. **Linear Basis**: To solve the "Max XOR Subset" problem, we use a Linear Basis. A Basis of size $\approx 20$ can represent the XOR space of values up to $2^{20}$.
4. **DFS Traversal**:
   - Traverse the Segment Tree. Maintain a current Linear Basis.
   - When entering a node, insert all values stored in that node into the current Basis.
   - If we reach a leaf (elementary interval), the Basis contains all active shields for that interval. Query the Basis for the maximum XOR sum. Update the global maximum.
   - When returning from recursion, the Basis state naturally reverts (if we passed a copy) or we can manage a stack. Passing a copy is feasible since Basis is small (size 20).

## Complexity
- **Time**: $O(N \log N \cdot B)$, where $B \approx 20$ is the number of bits.
  - Coordinate compression: $O(N \log N)$.
  - Building SegTree (updates): $N$ updates, each adds value to $\log N$ nodes. Total values added: $N \log N$.
  - DFS: Each value is inserted into a basis once. Total insertions $N \log N$. Each insertion takes $O(B)$ or $O(B^2)$ depending on implementation. Since we just check against basis size, it's fast.
- **Space**: $O(N \log N)$ to store values in the Segment Tree.

## Implementation Details
- Use `sys.setrecursionlimit` in Python.
- Fast I/O.
- Linear Basis insertion is greedy: try to XOR `val` with basis elements to reduce it. If result > 0, insert.

## Why this works
The "Max XOR Subset" property is efficiently maintained by a Linear Basis. The "Intersection of Intervals" property is efficiently handled by a Segment Tree. This approach combines them to solve the problem for all $X$ simultaneously.
