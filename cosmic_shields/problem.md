# Problem: Cosmic Shields

**Time Limit**: 2.0 seconds
**Memory Limit**: 256 MB

## Statement

You are the Chief Defense Architect of a space station. There are $N$ shield generators available. The $i$-th shield generator protects the linear region $[L_i, R_i]$ (inclusive) and operates at a frequency $S_i$.

At any specific integer coordinate $X$, a subset of shields is "active" if and only if $L_i \le X \le R_i$ for all shields in the subset.

The **Protection Level** at coordinate $X$ is defined as the maximum possible XOR sum of frequencies of any subset of shields that are active at $X$. (Note: The empty subset has an XOR sum of 0).

Your task is to determine the **maximum Protection Level** achievable at any integer coordinate $X$.

## Input

The first line contains an integer $T$ ($1 \le T \le 10$) — the number of test cases.

For each test case:
- The first line contains an integer $N$ ($1 \le N \le 50,000$).
- The following $N$ lines describe the shields. The $i$-th line contains three integers $L_i, R_i, S_i$ ($1 \le L_i \le R_i \le 10^9$, $1 \le S_i < 2^{20}$).

## Output

For each test case, output a single integer: the maximum Protection Level possible at any coordinate.

## Example

**Input**
```
2
3
1 5 3
2 6 5
4 8 4
2
1 10 7
20 30 7
```

**Output**
```
7
7
```

**Explanation**
Case 1:
Shields:
1. `[1, 5]`, val=3 (011)
2. `[2, 6]`, val=5 (101)
3. `[4, 8]`, val=4 (100)

At $X=4$, active shields are {1, 2, 3} with values {3, 5, 4}.
- $3 = 011_2$
- $5 = 101_2$
- $4 = 100_2$

Possible XOR sums:
- Single: 3, 5, 4
- Pairs: $3 \oplus 5 = 6$, $3 \oplus 4 = 7$, $5 \oplus 4 = 1$
- Triple: $3 \oplus 5 \oplus 4 = 2$
The maximum is 7.

Case 2:
The two shields never overlap. The maximum possible value is just the max of any single shield (since subsets size > 1 are impossible at any X). Max is 7.

## Constraints
$1 \le T \le 5$
$1 \le N \le 50,000$ (Sum of N over test cases $\le 50,000$)
$1 \le L_i \le R_i \le 10^9$
$0 \le S_i < 2^{20}$

## Notes
- A subset can be a single shield.
- The coordinates $X$ are integers.
