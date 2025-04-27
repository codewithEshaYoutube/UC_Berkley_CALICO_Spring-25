class Block:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.mass = (x1 - x0) * (y1 - y0)
        self.cm_x = (x0 + x1) / 2
        self.cm_y = (y0 + y1) / 2
        self.resting_on = None

def calculate_center_of_mass(blocks, idx):
    total_mass = blocks[idx].mass
    total_cm_x = blocks[idx].cm_x * blocks[idx].mass
    total_cm_y = blocks[idx].cm_y * blocks[idx].mass
    stack = [idx]
    while stack:
        current = stack.pop()
        if blocks[current].resting_on is not None:
            rest_idx = blocks[current].resting_on
            total_mass += blocks[rest_idx].mass
            total_cm_x += blocks[rest_idx].cm_x * blocks[rest_idx].mass
            total_cm_y += blocks[rest_idx].cm_y * blocks[rest_idx].mass
            stack.append(rest_idx)
    cm_x = total_cm_x / total_mass
    cm_y = total_cm_y / total_mass
    return cm_x, cm_y, total_mass

def check_stability(blocks):
    for idx, block in enumerate(blocks):
        if block.resting_on is not None:
            rest_idx = block.resting_on
            cm_x, cm_y, total_mass = calculate_center_of_mass(blocks, idx)
            resting_block = blocks[rest_idx]
            if not (resting_block.x0 <= cm_x <= resting_block.x1):
                return "Unstable"
    return "Stable"

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        blocks = []
        for i in range(N):
            x0, y0, x1, y1 = map(int, input().split())
            blocks.append(Block(x0, y0, x1, y1))
        for i in range(N):
            for j in range(i + 1, N):
                if blocks[i].x0 <= blocks[j].cm_x <= blocks[i].x1 and blocks[i].y1 == blocks[j].y0:
                    blocks[j].resting_on = i
        result = check_stability(blocks)
        print(result)

solve()
