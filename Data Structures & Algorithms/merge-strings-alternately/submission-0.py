class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        pointers = [iter(word1), iter(word2)]
        i = 0
        while True:
            try:
                # if len(pointers) == 0:
                #     break
                char = next(pointers[i])
                i = (i + 1) % len(pointers)
                result.append(char)
            except StopIteration:
                del pointers[i]
                print(pointers)
                i = 0
            except IndexError:
                break
        return "".join(result)