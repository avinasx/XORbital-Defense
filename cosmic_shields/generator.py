
import random
import sys

def generate():
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
        random.seed(seed)
        
    T = 5
    print(T)
    
    for _ in range(T):
        N = random.randint(1, 100) # Small for BF check, can be larger
        print(N)
        coord_range = 1000
        for _ in range(N):
            l = random.randint(1, coord_range - 10)
            r = random.randint(l, coord_range)
            s = random.randint(1, 100)
            print(f"{l} {r} {s}")

if __name__ == '__main__':
    generate()
