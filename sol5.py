def count_total_uwu_subsequences(given_input_string):

    list_of_u_letter_positions = []  # This list will store the positions (indexes) of all 'u' letters in the string
    # Find and store positions of all 'u' characters
    for current_character_index in range(len(given_input_string)):
        if given_input_string[current_character_index] == 'u':
            list_of_u_letter_positions.append(current_character_index)
    total_uwu_subsequences_found = 0  # This will keep track of the number of "uwu" subsequences found
    # Check all possible pairs of 'u' characters
    for first_u_letter_index in range(len(list_of_u_letter_positions)):
        for second_u_letter_index in range(first_u_letter_index + 1, len(list_of_u_letter_positions)):
            # Now we check if there is any 'w' character between these two 'u' characters
            for character_between_us_index in range(list_of_u_letter_positions[first_u_letter_index] + 1, list_of_u_letter_positions[second_u_letter_index]):
                if given_input_string[character_between_us_index] == 'w':
                    total_uwu_subsequences_found += 1  # If a 'w' is found, this forms a "uwu" subsequence
                    break  # No need to search further between this pair once we find one 'w'
    return total_uwu_subsequences_found

list_of_input_strings = ["uwwu", "uyuwuuxuwu", "uuwuu", "wwuuouw"]  # List of strings to test
for current_test_string in list_of_input_strings:
    uwu_subsequence_count = count_total_uwu_subsequences(current_test_string)
    print(f'The number of "uwu" subsequences in "{current_test_string}" is: {uwu_subsequence_count}')