class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        news=''.join(c for c in s if c.isalnum())
        revs=news[::-1]
        if(revs==news):
            return True
        else:
            return False
