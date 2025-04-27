from collections import deque

drift_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def min_actions_to_visit_all_buttons(n, m, drift, grid):
    button_pos = {}
    for i in range(n):
        for j in range(m):
            button_pos[grid[i][j]] = (i, j)
    
    cursor = (0, 0)
    drift_len = len(drift)
    drift_idx = 0
    total_actions = 0
    visited = set()
    
    for button in range(1, n * m + 1):
        if grid[cursor[0]][cursor[1]] == button:
            continue
        
        target = button_pos[button]
        queue = deque([(cursor, drift_idx, 0)])
        visited.add((cursor, drift_idx))
        
        while queue:
            pos, d_idx, steps = queue.popleft()
            d = drift[(d_idx + steps) % drift_len]
            drift_delta = drift_map[d]
            
            for action in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = (pos[0] + action[0]) % n
                nc = (pos[1] + action[1]) % m
                nr = (nr + drift_delta[0]) % n
                nc = (nc + drift_delta[1]) % m
                next_pos = (nr, nc)
                next_drift = (d_idx + steps + 1) % drift_len
                
                if (next_pos, next_drift) in visited:
                    continue
                
                visited.add((next_pos, next_drift))
                
                if next_pos == target:
                    total_actions += steps + 1
                    cursor = next_pos
                    drift_idx = next_drift
                    queue.clear()
                    break
                
                queue.append((next_pos, next_drift, steps + 1))
    
    return total_actions

def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n, m = map(int, input().split())
        drift = input().strip()
        grid = [list(map(int, input().split())) for _ in range(n)]
        
        result = min_actions_to_visit_all_buttons(n, m, drift, grid)
        print(result)

if __name__ == "__main__":
    main()
