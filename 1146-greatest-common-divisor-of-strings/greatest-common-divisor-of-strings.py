class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        gcd_len = gcd(len(str1), len(str2))
        candidate = str1[:gcd_len]

        if str1 == candidate * (len(str1) // gcd_len) and str2 == candidate * (len(str2) // gcd_len):
            return candidate
        else:
            return ""
        