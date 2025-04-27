def count_uwu_subsequences_in_string(input_string):

    positions_of_u_characters = []  # This list will store the positions (indexes) of all 'u' characters in the string
    # Find and store positions of all 'u' characters
    for current_char_index in range(len(input_string)):
        if input_string[current_char_index] == 'u':
            positions_of_u_characters.append(current_char_index)
    
    total_uwu_count = 0  # This will keep track of the number of "uwu" subsequences found
    
    # Check all possible pairs of 'u' characters
    for first_u_index in range(len(positions_of_u_characters)):
        for second_u_index in range(first_u_index + 1, len(positions_of_u_characters)):
            # Now we check if there is any 'w' character between these two 'u' characters
            for index_between_us in range(positions_of_u_characters[first_u_index] + 1, positions_of_u_characters[second_u_index]):
                if input_string[index_between_us] == 'w':
                    total_uwu_count += 1  # If a 'w' is found, this forms a "uwu" subsequence
                    break  # No need to search further between this pair once we find one 'w'
    
    return total_uwu_count

input_test_strings = ["uwwu", "uyuwuuxuwu", "uuwuu", "wwuuouw"]  # List of strings to test
for current_test_string in input_test_strings:
    uwu_count_result = count_uwu_subsequences_in_string(current_test_string)
    print(f'The number of "uwu" subsequences in "{current_test_string}" is: {uwu_count_result}')
