class Concatenation:
    def find_word_concatenation(self,given,words):
        result=[]
        words_frequency={}
        for word in words:
            words_frequency[word]=1+words_frequency.get(word,0)
        word_count=len(words)
        word_length=len(words[0])
        for i in range(len(given)-word_count*word_length+1):
            words_seen={}
            for j in range(word_count):
                next_word_index=i+j*word_length
                word=given[next_word_index:next_word_index+word_length]
                if  word not in words_frequency:
                    break
                words_seen[word]=1+words_seen.get(word,0)
                if words_seen[word]>words_frequency.get(word,0):
                    break
                if j+1==word_count:
                    result.append(i)
                    print(result)
        return result

c=Concatenation()
assert c.find_word_concatenation("catfoxcat",["cat", "fox"])==[0,3]
assert c.find_word_concatenation("catcatfoxfox",["cat", "fox"])==[3]



