class Substring:
    def find_substring(self,str,pattern):
        pattern_count={}
        str_count={}
        for i in pattern:
            pattern_count[i]=1+pattern_count.get(i,0)
        need=len(pattern_count)
        have=0
        minimum=float("inf")
        result=[-1,-1]
        l=0
        for r in range(len(str)):
            right=str[r]
            str_count[right]=1+str_count.get(right,0)
            if right in pattern_count and str_count[right]==pattern_count[right]:
                have+=1
            while have==need:
                if (r-l+1)<minimum:
                    result=[l,r]
                    minimum=r-l+1
                str_count[str[l]]-=1
                if str[l] in pattern_count and pattern_count[str[l]]>str_count[str[l]]:
                    have-=1
                l+=1
        l,r=result
        if minimum!=float("inf"):
            return str[l:r+1]
        else:
            return ""
s=Substring()
assert s.find_substring("aabdec","abc")=="abdec"
assert s.find_substring("abdabca","abc")=="abc"
assert s.find_substring("adcad","abc")==""
                
