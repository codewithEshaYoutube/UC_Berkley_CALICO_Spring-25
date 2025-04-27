def solve_cylinder():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        
        # Store all points
        eesha_points = []
        for _ in range(n):
            x, y, z = map(float, input().split())
            eesha_points.append((x, y, z))
        
        # Find all unique x, y, and z coordinates
        eesha_x_vals = set()
        eesha_y_vals = set()
        eesha_z_vals = set()
        
        for eesha_x, eesha_y, eesha_z in eesha_points:
            eesha_x_vals.add(eesha_x)
            eesha_y_vals.add(eesha_y)
            eesha_z_vals.add(eesha_z)
        
        # Convert to lists and sort
        eesha_x_vals = sorted(list(eesha_x_vals))
        eesha_y_vals = sorted(list(eesha_y_vals))
        eesha_z_vals = sorted(list(eesha_z_vals))
        
        # For a rectangular prism, we expect exactly 2 unique values for each coordinate
        # But since points can be anywhere on the surface, we need to find the most frequent ones
        eesha_x_counts = {}
        eesha_y_counts = {}
        eesha_z_counts = {}
        
        for eesha_x, eesha_y, eesha_z in eesha_points:
            eesha_x_counts[eesha_x] = eesha_x_counts.get(eesha_x, 0) + 1
            eesha_y_counts[eesha_y] = eesha_y_counts.get(eesha_y, 0) + 1
            eesha_z_counts[eesha_z] = eesha_z_counts.get(eesha_z, 0) + 1
        
        # Find the most common x, y, z values which will represent the faces of the prism
        eesha_x_faces = sorted([(count, x) for x, count in eesha_x_counts.items()], reverse=True)[:2]
        eesha_y_faces = sorted([(count, y) for y, count in eesha_y_counts.items()], reverse=True)[:2]
        eesha_z_faces = sorted([(count, z) for z, count in eesha_z_counts.items()], reverse=True)[:2]
        
        # Extract the coordinate values for the faces
        eesha_x_min, eesha_x_max = min(eesha_x_faces[0][1], eesha_x_faces[1][1]), max(eesha_x_faces[0][1], eesha_x_faces[1][1])
        eesha_y_min, eesha_y_max = min(eesha_y_faces[0][1], eesha_y_faces[1][1]), max(eesha_y_faces[0][1], eesha_y_faces[1][1])
        eesha_z_min, eesha_z_max = min(eesha_z_faces[0][1], eesha_z_faces[1][1]), max(eesha_z_faces[0][1], eesha_z_faces[1][1])
        
        # Calculate dimensions
        eesha_length = eesha_x_max - eesha_x_min
        eesha_width = eesha_y_max - eesha_y_min
        eesha_height = eesha_z_max - eesha_z_min
        
        # Calculate volume
        eesha_volume = eesha_length * eesha_width * eesha_height
        
        # Print with required precision
        print(f"{eesha_volume:.2f}")

if __name__ == "__main__":
    solve_cylinder()