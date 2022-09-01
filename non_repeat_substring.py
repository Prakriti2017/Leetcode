class Substring:
    def no_repeat_substring(self,str):
        strings=set()
        l=0
        max_length=float("-inf")
        for r in range(len(str)):
            while str[r] in strings:
                strings.remove(str[l])
                l+=1
            strings.add(str[r])
            max_length=max(max_length,r-l+1)
        return max_length

s=Substring()
assert s.no_repeat_substring("aabccbb")==3
            



