
import random
import os
import subprocess

def generate_case(filename, type_idx):
    with open(filename, 'w') as f:
        # Single test case per file for simplicity in this structure?
        # Standard Codeforces has T test cases. I will put T=1 or T=small.
        T = 1
        f.write(f"{T}\n")
        
        if type_idx == 1:
            # Example
            f.write("3\n")
            f.write("1 5 3\n")
            f.write("2 6 5\n")
            f.write("4 8 4\n") # Modified to 4 to match my derivation of 7
            
        elif type_idx == 2:
            # Small Random
            N = 100
            f.write(f"{N}\n")
            for _ in range(N):
                l = random.randint(1, 1000)
                r = random.randint(l, 1000)
                s = random.randint(1, 1023)
                f.write(f"{l} {r} {s}\n")
                
        elif type_idx == 3:
            # Medium Random
            N = 1000
            f.write(f"{N}\n")
            for _ in range(N):
                l = random.randint(1, 100000)
                r = random.randint(l, l + 1000)
                s = random.randint(1, 1048575)
                f.write(f"{l} {r} {s}\n")
                
        elif type_idx == 4:
            # Large Sparse
            N = 50000
            f.write(f"{N}\n")
            for _ in range(N):
                l = random.randint(1, 10**9 - 10000)
                r = random.randint(l, l + random.randint(1, 10000))
                s = random.randint(1, 1048575)
                f.write(f"{l} {r} {s}\n")
                
        elif type_idx == 5:
            # Large Dense/Nested (The "Killer" test)
            N = 50000
            f.write(f"{N}\n")
            center = 500000
            for i in range(N):
                # Many intervals overlapping at center
                width = random.randint(1, 1000)
                if i % 2 == 0:
                    l = center - width
                    r = center + width
                else:
                    l = random.randint(1, 1000)
                    r = random.randint(l, 1000000)
                s = random.randint(1, 1048575)
                f.write(f"{l} {r} {s}\n")

def solve_case(in_file, out_file):
    # Run solution.py
    cmd = f"python3 cosmic_shields/solution.py < {in_file} > {out_file}"
    subprocess.run(cmd, shell=True, check=True)

def main():
    os.makedirs("cosmic_shields/test_cases", exist_ok=True)
    for i in range(1, 6):
        in_path = f"cosmic_shields/test_cases/{i}.in"
        out_path = f"cosmic_shields/test_cases/{i}.out"
        print(f"Generating {in_path}...")
        generate_case(in_path, i)
        print(f"Solving to {out_path}...")
        solve_case(in_path, out_path)

if __name__ == "__main__":
    main()
