class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
                "2": ("a","b","c"), "3":("d","e","f"), "4":("g","h","i"),
                "5": ("j","k","l"), "6": ("m","n","o"), "7":("p","q","r","s"),
                "8": ("t","u","v"), "9": ("w","x","y","z")
            }
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return dic[digits]

        combinations = []
        for digit in digits:
            combinations.append(dic[digit])

        left = 4 - len(combinations)
        for i in range(left):
            combinations.append([""])

        l = [(a+b+c+d) for a in combinations[0] for b in combinations[1] for c in combinations[2] for d in combinations[3]]

        return l     