def count_charac(str1):
    count = 0  # Step 2: Initialize a variable count to 0 to keep track of the count of characters

    for char in str1:
        count += 1
        # Step 3: Loop through each character in the input string

    # Step 4: For each character, increment the count by 1

    return count

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)