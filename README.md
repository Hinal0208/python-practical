# Python Practical Assignment


1. **Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.**

```python
def convert_number_to_word(next: int, numeric_word: str, string: str) -> str:
    if next < len(string):
        index = string[next]
        numeric_word += number_to_word[int(index)]
        res = convert_number_to_word(next+1, numeric_word, string)
        if res != "":
            return res
    else:
        return numeric_word
```

2. **Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.**

```Python
 if left == right == range_:
        n.append("".join(res))
        return
    if left < range_:
        res.append("(")
        generate_par(left+1,right,range_)
        res.pop()

    if left > right:
        res.append(")")
        generate_par(left,right+1,range_)
        res.pop()
```
 3. **Given an array of strings strs, group the anagrams together. You can return the answer in any order.**
 ```Python
 def get_anagrams(wordlist:list)-> list:


    anagrams = defaultdict(list)
    for word in wordlist:
        key =  "".join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())
 ```