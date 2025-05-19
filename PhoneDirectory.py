from collections import deque

class PhoneDirectory:
    """
    Approach:
    1. Use a queue (`available`) to hold numbers that can be assigned.
    2. Use a set (`used`) to track numbers that are currently assigned.
    3. On `get()`: pop from the queue and mark as used.
    4. On `check(number)`: return True if number is not in `used`.
    5. On `release(number)`: if number is in `used`, remove it and add back to queue.

    Time Complexity:
    - get(): O(1)
    - check(): O(1)
    - release(): O(1)

    Space Complexity:
    - O(N) for queue and set where N is the maxNumbers
    """

    def __init__(self, maxNumbers: int):
        self.available = deque(range(maxNumbers))
        self.used = set()

    def get(self) -> int:
        if not self.available:
            return -1
        num = self.available.popleft()
        self.used.add(num)
        return num

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.available.append(number)
