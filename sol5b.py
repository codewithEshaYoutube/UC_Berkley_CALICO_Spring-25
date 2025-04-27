def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(count_uwu(s))

def count_uwu(s):
    n = len(s)
    result = 0
    prefix_u = 0
    
    # Pre-compute suffix counts of 'u's
    suffix_u = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix_u[i] = suffix_u[i+1]
        if s[i] == 'u':
            suffix_u[i] += 1
    
    # Count u's before each position and use pre-computed suffix counts
    for i in range(n):
        if s[i] == 'u':
            prefix_u += 1
        elif s[i] == 'w':
            # Use pre-computed suffix count of 'u's after this position
            result += prefix_u * suffix_u[i+1]
    
    return result

if __name__ == "__main__":
    solve()