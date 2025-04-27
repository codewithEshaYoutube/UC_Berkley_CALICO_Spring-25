import sys
import threading

def calculate_center_of_mass(blocks, block_idx, children, visited):
    total_mass = blocks[block_idx]['mass']
    total_cx = blocks[block_idx]['mass'] * blocks[block_idx]['cx']
    total_cy = blocks[block_idx]['mass'] * blocks[block_idx]['cy']

    for child_idx in children[block_idx]:
        child_mass, child_cx, child_cy = calculate_center_of_mass(blocks, child_idx, children, visited)
        total_mass += child_mass
        total_cx += child_mass * child_cx
        total_cy += child_mass * child_cy

    if block_idx != -1:
        parent_block = blocks[block_idx]
        center_x = total_cx / total_mass
        if not (parent_block['x0'] <= center_x <= parent_block['x1']):
            visited['stable'] = False

    return total_mass, total_cx / total_mass, total_cy / total_mass

def process_test_case():
    N = int(sys.stdin.readline())
    blocks = []

    for _ in range(N):
        x0, y0, x1, y1 = map(int, sys.stdin.readline().split())
        mass = (x1 - x0) * (y1 - y0)
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        blocks.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'mass': mass, 'cx': cx, 'cy': cy})
    
    parents = [-1] * N
    children = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if blocks[i]['y0'] == blocks[j]['y1']:
                if not (blocks[i]['x1'] <= blocks[j]['x0'] or blocks[i]['x0'] >= blocks[j]['x1']):
                    parents[i] = j
                    children[j].append(i)
                    break

    visited = {'stable': True}

    for i in range(N):
        if parents[i] == -1 and blocks[i]['y0'] == 0:
            calculate_center_of_mass(blocks, i, children, visited)

    return "Stable" if visited['stable'] else "Unstable"

def main():
    sys.setrecursionlimit(10**6)
    T = int(sys.stdin.readline())
    for _ in range(T):
        print(process_test_case())

if __name__ == "__main__":
    threading.Thread(target=main).start()
