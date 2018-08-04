class Solution:
    def toLowerCase(self, str):
        res = ''
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'):
                res += chr(ord(s)- ord('A') + ord('a'))
            else:
                res += s
        return res
        # return str.lower()
        