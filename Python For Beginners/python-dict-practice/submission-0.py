from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    res = {}

    for char in word:
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1
    return res



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
