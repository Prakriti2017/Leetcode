class TwoPointers:
    def compare_strings(self,str1,str2):
        i=len(str1)
        j=len(str2)
        backspace=0
        while i>=0:
            if str1[i]=='#':
                backspace+=1
            elif backspace>0:
                backspace-=1
