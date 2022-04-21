class MyHashSet:
    # O(1) time | O(10^6 + 1) space
    def __init__(self):
        self.array = [False] * 1000001

    def add(self, key: int) -> None:
        self.array[key] = True

    def remove(self, key: int) -> None:
        self.array[key] = False

    def contains(self, key: int) -> bool:
        return self.array[key]
