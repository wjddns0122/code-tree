import sys

# Increase recursion depth just in case, though not needed for this approach
sys.setrecursionlimit(10**6)

def solve():
    # Read N and K
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n = int(line1[0])
        k = int(line1[1])
    except ValueError:
        return

    # Initialize difference array
    # Size N+2 to handle 1-based indexing and the r+1 index safely
    diff = [0] * (n + 2)

    for _ in range(k):
        try:
            line = sys.stdin.readline().split()
            if not line:
                break
            l = int(line[0])
            r = int(line[1])
            
            # Apply difference array logic
            diff[l] += 1
            diff[r + 1] -= 1
        except ValueError:
            break

    # Compute prefix sums to get actual values
    current_blocks = 0
    max_blocks = 0
    
    # Iterate from 1 to N
    for i in range(1, n + 1):
        current_blocks += diff[i]
        if current_blocks > max_blocks:
            max_blocks = current_blocks

    print(max_blocks)

if __name__ == "__main__":
    solve()