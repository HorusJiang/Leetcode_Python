class Solution:
    def uniqueMorseRepresentations(self, words):

        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        MorseAllSet = set()
        for letters in words:
            TransedWordsSet = ''
            for i in letters:
                TransedWordsSet += d[ord(i) - ord('a')]
            if TransedWordsSet != '':
                MorseAllSet.add(TransedWordsSet)
        return len(MorseAllSet)

        # return len({''.join(d[ord(i) - ord('a')]for i in w) for w in words})
