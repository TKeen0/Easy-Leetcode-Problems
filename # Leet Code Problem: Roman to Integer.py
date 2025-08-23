# Roman Numeral to Integer

#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)):
            cur = roman[s[i]]
            if i + 1 < len(s):
                nxt = roman[s[i+1]]
            else:
                nxt = 0

            if cur < nxt:
                    total -= cur
            else:
                    total += cur

            #print(f"index={i}, character={s[i]}, current={cur}, next={nxt}")
            #print("->total now:", total)
        return total

if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))