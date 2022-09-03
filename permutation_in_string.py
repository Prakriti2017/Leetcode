class StringPermutation:
    def find_permutation(self,have,need):
        l=0
        have_count=[0]*26
        need_count=[0]*26
        for i in range(len(need)):
            need_count[ord(need[i])-ord('a')]+=1
            have_count[ord(have[i])-ord('a')]+=1
        if have_count==need_count:
            return True
        for r in range(len(need),len(have)):
            if have_count==need_count:
                return True
            have_count[ord(have[r])-ord('a')]+=1
            have_count[ord(have[l])-ord('a')]-=1
            l+=1

        return False
    
p=StringPermutation()
assert p.find_permutation("oidbcaf","abc")==True
assert p.find_permutation("odicf","dc")==False
assert p.find_permutation("bcdxabcdy","bcdyabcdx")==True
        