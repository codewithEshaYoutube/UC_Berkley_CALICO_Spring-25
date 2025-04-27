def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(count_uwu(s))

def count_uwu(s):
    n = len(s)
    result = 0
    prefix_u = 0
    
    # Count u's before each position and process each w
    for i in range(n):
        if s[i] == 'u':
            prefix_u += 1
        elif s[i] == 'w':
            # For each w, find all u's after it
            suffix_u = 0
            for j in range(i+1, n):
                if s[j] == 'u':
                    suffix_u += 1
            
            # Each pair of (u_before, u_after) forms one valid subsequence
            result += prefix_u * suffix_u
    
    return result

if __name__ == "__main__":
    solve()