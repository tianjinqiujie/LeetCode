class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        last = 1001
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for char in s:
            number = mapping[char]
            result += number

            if last < number:
                result -= 2 * last
            last = number
        return result
a = Solution()
print(a.romanToInt("MCMXCIV"))