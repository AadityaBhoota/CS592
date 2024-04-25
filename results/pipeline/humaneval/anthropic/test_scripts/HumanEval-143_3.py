def words_in_sentence(sentence):
    max_word_length = max(len(word) for word in sentence.split())
    prime_lengths = get_prime_numbers(max_word_length)
    return ' '.join(word for word in sentence.split() if len(word) in prime_lengths and word.isalpha())

def get_prime_numbers(max_length):
    primes = set()
    for i in range(2, max_length + 1):
        if is_prime(i):
            primes.add(i)
    return primes

def is_prime(n):
    if n <= 1:
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