from collections import deque

def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n, m = map(int, input().split())
        drift = input().strip()
        grid = []
        button_positions = {}
        
        for i in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
            for j in range(m):
                button_positions[row[j]] = (i, j)
        
        cursor = (0, 0)
        drift_idx = 0
        total_actions = 0
        
        for button in range(1, n*m + 1):
            if grid[cursor[0]][cursor[1]] == button:
                continue
                
            actions = find_shortest_path(cursor, button, button_positions, grid, drift, drift_idx, n, m)
            total_actions += actions[0]
            cursor = actions[1]
            drift_idx = (drift_idx + actions[0]) % len(drift)
            
        print(total_actions)

def find_shortest_path(start, target_button, button_positions, grid, drift, drift_idx, n, m):
    queue = deque([(start, 0)])
    visited = set([(start, drift_idx % len(drift))])
    
    while queue:
        pos, steps = queue.popleft()
        current_drift = drift[(drift_idx + steps) % len(drift)]
        
        for action in ["NONE", "UP", "DOWN", "LEFT", "RIGHT"]:
            next_pos = move_with_drift(pos, action, current_drift, n, m)
            next_drift_idx = (drift_idx + steps + 1) % len(drift)
            
            if (next_pos, next_drift_idx) in visited:
                continue
                
            visited.add((next_pos, next_drift_idx))
            
            if grid[next_pos[0]][next_pos[1]] == target_button:
                return (steps + 1, next_pos)
                
            queue.append((next_pos, steps + 1))
    
    return (0, start)

def move_with_drift(pos, action, drift, n, m):
    row, col = pos
    
    if action == "UP":
        row = (row - 1) % n
    elif action == "DOWN":
        row = (row + 1) % n
    elif action == "LEFT":
        col = (col - 1) % m
    elif action == "RIGHT":
        col = (col + 1) % m
    
    if drift == "U":
        row = (row - 1) % n
    elif drift == "D":
        row = (row + 1) % n
    elif drift == "L":
        col = (col - 1) % m
    elif drift == "R":
        col = (col + 1) % m
    
    return (row, col)

if __name__ == "__main__":
    main()
