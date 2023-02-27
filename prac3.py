import time
from collections import defaultdict


def get_anagrams(wordlist:list)-> list:


    anagrams = defaultdict(list)
    for word in wordlist:
        key =  "".join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())



if __name__ == "__main__":

    start_time = time.perf_counter()
    strs =input("::")
    temp = strs.split(',')
    ans  = get_anagrams(temp)
    print(ans)
    end_time = time.perf_counter()
    print(end_time-start_time)

