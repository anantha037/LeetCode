class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        result =[]
        for word in words:
            mapping = {}
            visited_pattern_chars = set()
            is_valid = True
            for ch, p in zip(word, pattern):
                if ch not in mapping:
                    if p not in visited_pattern_chars:
                        mapping[ch] = p
                        visited_pattern_chars.add(p)
                    else:
                        is_valid = False
                        break
                else:
                    if mapping[ch] != p:
                        is_valid = False
                        break
                
            if is_valid:
                result.append(word)

        return result
        