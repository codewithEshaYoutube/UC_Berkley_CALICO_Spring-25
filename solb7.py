def solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Number of blocks
        
        # Read block data
        blocks = []
        for i in range(N):
            X0, Y0, X1, Y1 = map(int, input().split())
            blocks.append((X0, Y0, X1, Y1, (X1 - X0) * (Y1 - Y0), (X0 + X1) / 2, (Y0 + Y1) / 2))  # Append block details
        
        # We need to simulate the structure and check if it is stable
        
        # Structure to keep track of each block's center of mass and which block it rests on
        parent = [-1] * N  # -1 means no parent (resting on the floor)
        # Read the rest positions of blocks (if they rest on others)
        for i in range(1, N):
            parent[i] = int(input())  # For block i, it rests on the parent block
        
        # We need to calculate the center of mass for each block and substructure
        # Create a list to store the center of mass of each block and its combined substructure
        mass = [block[4] for block in blocks]
        cm = [(block[5], block[6]) for block in blocks]  # (center of mass x, center of mass y)
        
        # Check if the structure is stable or not
        def calculate_cm(i):
            if parent[i] == -1:  # It's on the floor
                return cm[i]
            else:
                # If it has a parent, calculate its combined center of mass with the parent
                px, py = calculate_cm(parent[i])  # Parent's center of mass
                p_mass = mass[parent[i]]
                total_mass = mass[i] + p_mass
                x_cm = (cm[i][0] * mass[i] + px * p_mass) / total_mass
                y_cm = (cm[i][1] * mass[i] + py * p_mass) / total_mass
                cm[i] = (x_cm, y_cm)
                return cm[i]
        
        # Calculate the center of mass for all blocks
        for i in range(N):
            calculate_cm(i)
        
        # Now check if the center of mass of any block is stable
        stable = True
        for i in range(N):
            if parent[i] != -1:
                px, py = cm[parent[i]]
                if not (blocks[parent[i]][0] <= cm[i][0] <= blocks[parent[i]][2]):
                    stable = False
                    break
        
        if stable:
            print("Stable")
        else:
            print("Unstable")

# Call the solve function to handle inputs and outputs
solve()
