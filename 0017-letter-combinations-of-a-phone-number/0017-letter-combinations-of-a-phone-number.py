class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        telephone = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }

        words = []

        for i in digits:
            curr = telephone[int(i)]
            if not words:
                for j in curr:
                    words.append(j)
            else:
                l = 0
                n = len(words)
                while l<n:
                    word = words[l]
                    to_add = []
                    for j in curr:
                        to_add.append(word+j)
                    words.extend(to_add)
                    l+=1
                    
        
        return [w for w in words if len(w) == len(digits)]


