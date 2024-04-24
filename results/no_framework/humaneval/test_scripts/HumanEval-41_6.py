To solve this problem, we can consider the scenario in a simpler way. Let's say we have `n` pairs of cars moving towards each other. If they all start at different positions and move with the same speed, there will be a collision if and only if the cars are exactly opposite each other.

If the distance between the cars is a multiple of the sum of their speeds, then they will collide as they reach the same point at the same time. Therefore, if two cars are `d` distance apart with speed `s`, the time taken by each car to reach the starting point of the other car is `d / (2*s)`.

To find the total number of collisions, we need to consider all possible pairs of cars. The total number of collisions would be the number of pairs of cars multiplied by the number of collisions each pair would have.

We can use the formula for combinations `nCr = n! / (r! * (n-r)!)` to find the number of ways to choose `2` cars out of `n`. The total number of collisions can then be calculated using the formula: `Collisions = nCr * collisions_per_pair`.

Let's implement this in the code:


METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)