def min_actions_to_visit_buttons(T, test_cases):
    results = []
    
    for case in test_cases:
        N, M, grid = case
        pos = {}
        for r in range(N):
            for c in range(M):
                pos[grid[r][c]] = (r, c)
        
        actions = 0
        current_r, current_c = 0, 0
        
        for num in range(1, N * M + 1):
            target_r, target_c = pos[num]
            vert_move = min(abs(current_r - target_r), N - abs(current_r - target_r))
            hori_move = min(abs(current_c - target_c), M - abs(current_c - target_c))
            actions += vert_move + hori_move
            current_r, current_c = target_r, target_c
        
        results.append(actions)
    
    return results


T = int(input())
test_cases = []

for _ in range(T):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    test_cases.append((N, M, grid))

answers = min_actions_to_visit_buttons(T, test_cases)

for ans in answers:
    print(ans)
