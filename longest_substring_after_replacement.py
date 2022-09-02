class Substring:
    def character_replacement(self,str,k):
        l=0
        frequency={}
        result=0
        for r in range(len(str)):
            frequency[str[r]]=1+frequency.get(str[r],0)
            while (r-l+1)-max(frequency.values())>k:
                frequency[str[l]]-=1
                l+=1
            result=max(result,r-l+1)

        return result


s=Substring()
s.character_replacement("aabccbb",2)==5
s.character_replacement("abbcb",1)==4