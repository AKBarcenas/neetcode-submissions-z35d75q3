class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += (str(len(string)) + "!" + string)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        index = 0
        while index < len(s):
            length = ""
            while s[index] != "!":
                length += s[index]
                index += 1
            
            index += 1
            wordLength = int(length)
            nextWord = ""

            for wordIndex in range(wordLength):
                nextWord += s[index + wordIndex]

            decodedStrings.append(nextWord)
            index += wordLength
        return decodedStrings