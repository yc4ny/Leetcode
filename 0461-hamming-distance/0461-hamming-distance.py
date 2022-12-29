class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        listx = []
        listy = []
        start1 = x
        start2 = y
        bool = True
        while(bool):
            if x > 1:
                listx.append(x%2)
                x = x // 2
            else:
                listx.append(1)
                bool = False

        bool = True
        while(bool):
            if y > 1:
                listy.append(y%2)
                y = y // 2
            else:
                listy.append(1)
                bool = False
        if start1 == 0:
            listx = [0]
        if start2 == 0:
            listy = [0]

        if len(listx) != len(listy):
            difference = abs(len(listx) -len(listy))
            new_list = []

            if len(listx) < len(listy):
                for i in range(len(listx)):
                    new_list.append(listx[i])
                    max_list = listy
            else:
                for i in range(len(listy)):
                    new_list.append(listy[i])
                    max_list = listx

            for i in range(difference):
                new_list.append(0)

            count = 0
            for i in range(len(max_list)):
                if max_list[i] != new_list[i]:
                    count += 1

        else:
            count = 0 
            for i in range(len(listx)):
                if listx[i] != listy[i]:
                    count += 1

        return count