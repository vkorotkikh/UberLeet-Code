from collections import Counter
import heapq
from typing import List

# ------------------------------------------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------------------------------------------

TEST_CASES = [
    (["i","love","leetcode","i","love","coding"], 2),
    (["the","day","is","sunny","the","the","the","sunny","is","is"], 4),
    (["hello","hello","hello","hello","hello"], 1),  # single unique word
    (["apple","banana","apple","banana","cherry"], 2),  # freq tie resolved lexicographically
    (["alpha","beta","gamma","delta","epsilon","zeta","eta","theta"], 3),  # all unique, k < len
    (["Cat","cat","dog","dog","dog","CAT","dog","cat"], 2),  # case sensitivity
    (["news","news","news","sports","sports","weather","finance","finance","finance","finance"], 3),  # dominant winner
    (["nlp","ml","ai","data","nlp","ml","ai","nlp","ml","ai","ml","nlp","ai","data"], 2),  # three-way tie stretched
    ("""to be or not to be that is the question whether tis nobler in the mind to suffer""".split(), 5),  # Shakespeare chunk
    ("""call me ishmael some years ago never mind how long precisely having little or no money in my purse""".split(), 4),  # prose slice
]

def topKFrequent_heap(words: List[str], k: int) -> List[str]:
    """
    Return top-k frequent words in a list using binary heap (priority queue).
    
    Algorithm Strategy:
    -------------------
    1. Counter words using Counter in O(n) time.
    2. Build a heap of tuples (-frequency, word) in O(U), where U is the number of unique words.
        - Using negative frequency turns min-heap into a max by frequency heap.
        - The second key word naturally enforces lexicographical ascending on ties.
    3. Pop top-k elements; each pop is O(log U); total O(k log(U)).
    
    Complexity Analysis:
    -------------------
    Time: O(N + U + k*log(U))
    Time: O(N) for counting freq, O(U) for building heap, O(k*log(U)) for popping top k elements
    Space: O(U)
    
    Why is space O(U)?
    -------------------
    We are storing the frequency of each word in a dictionary which takes O(U) space.
    """

    # Use Counter to count the frequency of each word in O(n) time.
    freq = Counter(words) # freq is a dictionary of word : frequency
    
    # Build a heap of tuples (-frequency, word) in O(U) time.
    heap = [(-f, w) for w, f in freq.items()]
    
    # use heapq.heapify to build a heap in O(U) time.
    heapq.heapify(heap)
    
    # Extract the top k elements from the heap in O(k*log(U)) time.
    result = [heapq.heappop(heap)[1] for _ in range(k)]
    
    return result

# Do full sort solution with Counter and sorted plus lambda function
def topKFrequent_sort(words: List[str], k: int) -> List[str]:
    """ 
    Sort all the unique words in a list by (-freq, word) and slice the first k elements.
    Full sort and simplest solution, but can be slower than heap for larger datasets.
    
    Complexity Analysis:
    -------------------
    Time: O(U log(U)) due to sorting unique words
    Space: O(U) due to storing unique words

    """
    # Use counter to count the frequency of each word in O(n) time.
    # Counter returns a dictionary of word : frequency
    count = Counter(words)
    
    # Sort the unique words by (-freq, word), inverting the frequency with - sign such that
    # the highest frequency starts first
    ordered = (sorted(count.keys(), key=lambda w: (-count[w], w)))
    
    # return first k elements via list slicing
    return ordered[:k]


def run_demo():
    solvers = {
        "heap_all": topKFrequent_heap,
        "sorted": topKFrequent_sort,
    }
    for label, func in solvers.items():
        print(f"{label}: {func.__doc__}")
        for words, k in TEST_CASES:
            print(func(words, k))

if __name__ == "__main__":
    run_demo()