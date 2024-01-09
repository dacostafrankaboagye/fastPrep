class MyHashSet:

    def __init__(self):
        self._hashset = []

    def add(self, key: int) -> None:
        if key not in self._hashset:
            self._hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self._hashset:
            self._hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._hashset


# Example usage:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))  # Output: True
print(obj.contains(3))  # Output: False
obj.add(2)
print(obj.contains(2))  # Output: True
obj.remove(2)
print(obj.contains(2))  # Output: False

        
