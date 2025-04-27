def count_uwu_subsequences(input_string):
    """
    This function will work like:
    
    This function counts how many "uwu" subsequences exist in the input string.
    
    A "uwu" subsequence is defined as a 'u' followed by a 'w' with another 'u' after it, 
    but the 'w' must be positioned between the two 'u' characters.

    Args:
        input_string (str): The string in which we want to search for "uwu" subsequences.

    Returns:
        int: The total number of "uwu" subsequences found in the string.
    """
    u_positions = []  # We will store the indices of 'u' characters here
    
    # Loop through the string to find all 'u' characters and note their positions
    for index in range(len(input_string)):
        if input_string[index] == 'u':
            u_positions.append(index)
    
    uwu_count = 0  # This will keep track of how many "uwu" subsequences we find
    
    # Now, for every pair of 'u's in the string, check if there's a 'w' between them
    for first_u_index in range(len(u_positions)):
        for second_u_index in range(first_u_index + 1, len(u_positions)):
            
            # Look at all characters between these two 'u's
            for middle_char_index in range(u_positions[first_u_index] + 1, u_positions[second_u_index]):
                if input_string[middle_char_index] == 'w':  # If 'w' is found, it completes the subsequence
                    uwu_count += 1  # Increase the count for this "uwu"
                    break  # No need to check further for this pair of 'u's, move on
    
    return uwu_count
# USED IN EXAMPLE HERE
test_strings = ["uwwu", "uyuwuuxuwu", "uuwuu", "wwuuouw"]  # A list of test strings
for test_string in test_strings:
    result = count_uwu_subsequences(test_string)
    print(f'The number of "uwu" subsequences in "{test_string}" is: {result}')
