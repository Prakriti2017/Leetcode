class Anagrams:
    def find_anagram_index(self,str,pattern):
        if len(pattern)>len(str):
            return []
        l=0
        indices=[]
        str_count=[0]*26
        pattern_count=[0]*26
        for i in range(len(pattern)):
            pattern_count[ord(pattern[i])-ord('a')]+=1
            str_count[ord(str[i])-ord('a')]+=1
        if pattern_count==str_count:
            indices.append(l)
        for r in range(len(pattern),len(str)):
            str_count[ord(str[r])-ord('a')]+=1
            str_count[ord(str[l])-ord('a')]-=1
            l+=1
            if pattern_count==str_count:
                indices.append(l)
        return indices

a=Anagrams()
assert a.find_anagram_index("ppqp","pq")==[1,2]
assert a.find_anagram_index("abbcabc","abc")==[2,3,4]


