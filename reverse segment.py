class Solution(object):
    def reversePrefix(self, word, ch):
        j = word.find(ch)
        if j != -1:
            return word[:j+1][::-1] + word[j+1:]
        return word  