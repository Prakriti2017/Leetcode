from turtle import isvisible


class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 1
        if n==1:
            return self.isValid(s)
        total=0
        if self.isValid(s[-1]):
            total+=self.numDecodings(s[:-1])
        if self.isValid(s[-2:]):
            total+=self.numDecodings(s[:-2])

        return total

    def isValid(self, s: str)->int:
        if len(s)==1 and int(s)!=0:
            return 1
        if len(s)==2 and 0<int(s[0])<=2 and int(s[1])<=6:
            return 1

        return 0
so=Solution()

assert so.isValid("0")==0
assert so.isValid("2")==1
assert so.isValid("26")==1
assert so.isValid("27")==0
assert so.isValid("06")==0
print("is valid tests completed")
assert so.numDecodings("0")==0
assert so.numDecodings("1")==1
assert so.numDecodings("12")==2
assert so.numDecodings("226")==3
assert so.numDecodings("2611055971756562")==4

print("nums decoding tests completed")
# print("1234"[:-2])

