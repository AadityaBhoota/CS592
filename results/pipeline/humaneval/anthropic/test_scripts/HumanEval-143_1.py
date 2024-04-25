def words_in_sentence(sentence):
    """
    Returns a string containing the words from the input sentence whose lengths are prime numbers.
    """
    words = sentence.split()
    max_word_len = max(len(word) for word in words)
    prime_numbers = get_prime_numbers(max_word_len)
    prime_words = [word for word in words if len(word) in prime_numbers]
    return ' '.join(prime_words)

def get_prime_numbers(max_len):
    """Helper function to get all prime numbers up to max_len"""
    primes = set()
    for i in range(2, max_len + 1):
        if is_prime(i):
            primes.add(i)
    return primes

def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(candidate):

    # Check some simple cases
    assert candidate("This is a test") == "is"
    assert candidate("lets go for swimming") == "go for"
    assert candidate("there is no place available here") == "there is no place"
    assert candidate("Hi I am Hussein") == "Hi am Hussein"
    assert candidate("go for it") == "go for it"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("here") == ""
    assert candidate("here is") == "is"


check(words_in_sentence)