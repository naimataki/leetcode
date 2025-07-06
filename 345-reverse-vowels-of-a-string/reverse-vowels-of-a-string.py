class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        
        # Collect vowels in a list
        s_vowels = [char for char in s if char in vowels]
        
        # Reverse the list of vowels
        s_vowels = s_vowels[::-1]
        
        # Build the new string
        result = []
        for char in s:
            if char in vowels:
                result.append(s_vowels.pop(0))
            else:
                result.append(char)
        
        return ''.join(result)



