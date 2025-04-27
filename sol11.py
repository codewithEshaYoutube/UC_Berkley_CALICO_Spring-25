def solve_cylinder():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        
        # Store all points
        eesha_points = []
        for _ in range(n):
            x, y, z = map(float, input().split())
            eesha_points.append((x, y, z))
        
        # Find min and max values for each coordinate
        eesha_min_x = float('inf')
        eesha_max_x = float('-inf')
        eesha_min_y = float('inf')
        eesha_max_y = float('-inf')
        eesha_min_z = float('inf')
        eesha_max_z = float('-inf')
        
        # Find the extreme coordinates
        for eesha_point in eesha_points:
            eesha_x, eesha_y, eesha_z = eesha_point
            
            eesha_min_x = min(eesha_min_x, eesha_x)
            eesha_max_x = max(eesha_max_x, eesha_x)
            eesha_min_y = min(eesha_min_y, eesha_y)
            eesha_max_y = max(eesha_max_y, eesha_y)
            eesha_min_z = min(eesha_min_z, eesha_z)
            eesha_max_z = max(eesha_max_z, eesha_z)
        
        # Calculate the dimensions of the rectangular prism
        eesha_length = eesha_max_x - eesha_min_x
        eesha_width = eesha_max_y - eesha_min_y
        eesha_height = eesha_max_z - eesha_min_z
        
        # Calculate the volume
        eesha_volume = eesha_length * eesha_width * eesha_height
        
        # Print with required precision (the problem accepts relative or absolute error < 10^-5)
        print(f"{eesha_volume:.2f}")

if __name__ == "__main__":
    solve_cylinder()