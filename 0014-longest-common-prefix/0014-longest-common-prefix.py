class Solution:
    def longestCommonPrefix(self, list: List[str]) -> str:
        length = len(list)
        if length == 1:
            return list[0]
        output = ""
        count = 0
        array = []
        #Shortest Length of Word 
        shortest_word = len(list[0])
        for i in range (0,length-1):
            if shortest_word > len(list[i+1]):
                shortest_word = len(list[i+1])

        if shortest_word == 0:
            return ""

        for i in range(0,length-1):
            for j in range(0,shortest_word):
                if list[i][j] == list[i+1][j]:
                    count += 1
                    if j == shortest_word -1:
                        array.append(count)
                        count = 0 
                else:
                    array.append(count)
                    count = 0
                    break


        if len(array) == 0:
            return ""
        else:
            for i in range (0, min(array)):
                output = output + list[0][i]
            return output 