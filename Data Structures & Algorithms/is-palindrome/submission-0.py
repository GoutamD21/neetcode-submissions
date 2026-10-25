
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stripd = s.replace(" ","")
        stripd = re.sub(r'[^a-zA-Z0-9]', '', s)
        fwd = stripd
        for i in range(len(s)):
            bkwd = fwd[::-1]
    
        if fwd.casefold() != bkwd.casefold():
            return False
        return True