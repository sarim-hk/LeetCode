class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, v in enumerate(reversed(digits)):
            num += (v*(10**(i)))
        num += 1

        return [int(digit) for digit in str(num)]
