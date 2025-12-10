# Cosmic Shields - Competitive Programming Problem

A Div1-C / Div2-E level problem involving Segment Trees, Linear Basis, and Coordinate Compression.

## Folder Structure
- **problem.md**: The full problem statement.
- **solution.md**: Explanation of the optimal solution.
- **solution.py**: Python implementation of the $O(N \log N \cdot B)$ solution.
- **requirements.json**: Problem metadata and limits.
- **idea.md**: Problem conception and refinement log.
- **qwen/**: Simulated attempts by a strong LLM showing failure modes.
- **test_cases/**: 5 strong test cases (Input `.in` and Expected Output `.out`).
- **generator.py**: Script used to generate random test cases.
- **solution_bf.py**: Brute force solution for verification.

## How to Run
1. Generate test cases (if needed):
   ```bash
   python3 generator.py
   # Or use the specific script:
   python3 generate_cases_script.py (if available)
   ```
2. Run optimal solution:
   ```bash
   python3 solution.py < test_cases/1.in
   ```
3. Run brute force check:
   ```bash
   python3 solution_bf.py < test_cases/1.in
   ```

## Requirements check
- [x] Original Problem (Intersection + Basis)
- [x] Qwen Fails (Brute Force, Pruning, Resampling)
- [x] Test Cases (5 Strong cases generated)
- [x] Documentation complete
