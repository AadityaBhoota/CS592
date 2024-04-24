To solve this problem, we can make use of combinatorial mathematics. Since each car moving left to right can collide with any car moving right to left, we can simply calculate the number of possible pairs that can collide.

The total number of collisions can be calculated by the formula:
\[ \text{Total Collisions} = \frac{n(n-1)}{2} \]

Let's implement this logic in the function:


METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)