class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0