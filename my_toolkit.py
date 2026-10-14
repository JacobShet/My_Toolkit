def calculate_average(numbers):
    '''
    Calculate the average of a list of numbers. 
    If the list of numbers is empty, returns 0.
    Otherwise calculate the average and return the nearest whole number.

    Args: 
        numbers (list), A list of numbers to average

    Returns:
        float: the average(rounded), 
        int: 0 if the list is empty
    '''
    if len(numbers) == 0:       # Check if the list of numbers is empty
        return 0

    total = 0                   

    for number in numbers:      # Add the numbers in the list together 
        total += number

    return round(total / len(numbers), 0)       # Calculate the average.

def find_max_and_min(numbers):
    '''
    Calculate the largest and smallest numbers in a list. 

    Args: 
        numbers (list), A list of numbers to calculate the maximum and minimum value of.

    Returns:
        tuple: A tuple containing the largest and smallest numbers.  str: "List empty" if the list is empty.

    '''
    try:
        max_value = numbers[0]
        min_value = numbers[0]

        for number in numbers:              # Loop over the numbers, compare each number and update the max_value and min_value when necessary.
            if number > max_value:
                max_value = number
            elif number < min_value:
                min_value = number

        return max_value, min_value
    except IndexError:                      
        return "List empty"                  # Return "List empty" If the list passed to the function has no values

def count_occurrences(items, target):
    '''
    Counts how many times a target appears in a list.

    Args: 
        items (list): A list of items to search
        target: The value to search for in the list

    Returns:
        int: The number of times the target value appears in the list. 
    '''
    counter = 0                                 

    for item in items:
        if item == target:
            counter += 1                        # If a target value is found in the list, increment the counter by 1
    return counter

def is_palindrome(text):
    '''
    Compares text to see if it is the same forward and backwards regardless of capitalization or spaces.

    Args:
        text (str): the text to check for a palindrome.

    Return:
        bool: True if the text is a palindrome.
        False otherwise.
    '''
    text = text.lower().replace(" ", "")        # Format the string so that capitalization and spaces are ignored

    if text == text[::-1]:                      # Run a check reversing the string and compares to see if its the same as normal
        return True
    else:
        return False

def create_report(title, scores):
    '''
    Generates a formatted report using the scores provided.

    Args:
        title (str): The title of the report.
        scores (list): A list of integers to analyze.

    Returns:
        str: A formatted output containing the average, highest, and lowest scores.
        str: "N/A" if the list is empty
    '''
    average = calculate_average(scores)
    max_and_min = find_max_and_min(scores)

    if max_and_min == "List empty":
        highest = "N/A"
        lowest = "N/A"
    else:
        highest, lowest = max_and_min
        

    # Create and return a formatted report
    report = f"""{title}
=== Report ===
Average: {average}
Highest: {highest}
Lowest:  {lowest}
=============="""

    return report


# Testing

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    edge_case_empty_list = []
    edge_case_repeating_target = [85, 92, 78, 95, 85, 88, 70, 93, 85, ]

    print(f"Average:  {calculate_average(test_scores)}")
    print(f"Max/Min:  {find_max_and_min(test_scores)}")
    print(f"Count of 85:  {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome:  {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    # Edge cases
    print()
    print("=" * 40)
    print("     Edge Cases")
    print("=" * 40)
    print(f"Edge case average: {calculate_average(edge_case_empty_list)}")
    print(f"Edge case max/min: {find_max_and_min(edge_case_empty_list)}")
    print(f"Edge case count of 85:  {count_occurrences(edge_case_repeating_target, 85)}")
    print(f"Edge case count_occurences with a missing target: {count_occurrences(test_scores, 106)}")
    print(f"'Noon' palindrome: {is_palindrome('Noon')}")
    print(f"'A man a plan a canal Panama' palindrome:  {is_palindrome('A man a plan a canal Panama')} \n")
    print(create_report("Edge case create_report with an empty list:", edge_case_empty_list), "\n")
    print("=" * 40)

