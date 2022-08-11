class Solution:
    def findKangarooScore(self,words,wordsToSynonyms,wordsToAntonyms):
        i=0
        while(i<len(words)):
            if(words[i] in wordsToSynonyms.keys()):
                for v in wordsToSynonyms.values():
                    if(words[i]==v[]):
                        
            i+=1
    
        return words
s=Solution()
s.findKangarooScore(["animosity","encourage"],{"encourage":["urge","boost","inspire"],"animosity":["hate"]},{"animosity":["amity","like"]})
