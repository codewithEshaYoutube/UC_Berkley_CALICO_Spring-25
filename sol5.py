def count_uwu_subsequences(input_string):
    """
    Counts how many "uwu" subsequences are present in the given string.
    
    A "uwu" subsequence is defined as a 'u' followed by a 'w' with another 'u' after it, 
    but the 'w' must be positioned between the two 'u' characters.
    
    Args:
        input_string (str): The string in which we want to find "uwu" subsequences.
        
    Returns:
        int: The total number of "uwu" subsequences found in the input string.
    """
    u_positions = []  # This list stores the positions of 'u' characters
    
    # Loop through the string to find all 'u' characters and store their positions
    for index in range(len(input_string)):
        if input_string[index] == 'u':
            u_positions.append(index)
    
    uwu_count = 0  # Counter for the number of "uwu" subsequences
    
    # For each pair of 'u's, check if there's a 'w' between them
    for first_u_index in range(len(u_positions)):
        for second_u_index in range(first_u_index + 1, len(u_positions)):
            
            # Check if there's a 'w' between these two 'u's
            for middle_char_index in range(u_positions[first_u_index] + 1, u_positions[second_u_index]):
                if input_string[middle_char_index] == 'w':
                    uwu_count += 1  # If 'w' is found, count it as a "uwu" subsequence
                    break  # No need to check further once a valid subsequence is found
    
    return uwu_count


# --- Example usage ---
test_strings = ["uwwu", "uyuwuuxuwu", "uuwuu", "wwuuouw"]  # A list of strings to test
for test_string in test_strings:
    result = count_uwu_subsequences(test_string)
    print(f'The number of "uwu" subsequences in "{test_string}" is: {result}')
