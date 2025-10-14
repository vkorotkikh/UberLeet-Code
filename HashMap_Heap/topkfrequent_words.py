from collections import Counter
import heapq
from typing import List

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
    Space: O(U)
    
    Why is space O(U)?
    -------------------
    We are storing the frequency of each word in a dictionary which takes O(U) space.
    """

    # Use conter to count the frequency of each word in O(n) time.
    freq = Counter(words) # freq is a dictionary of word : frequency
    
    # Build a heap of tuples (-frequency, word) in O(U) time.
    heap = [(-f, w) for w, f in freq.items()]
    
    # use heapq.heapify to build a heap in O(U) time.
    heapq.heapify(heap)
    
    # Extract the top k elements from the heap in O(k*log(U)) time.
    result = [heapq.heappop(heap)[1] for _ in range(k)]
    
    return result

# Do full sort solution with Counter and sorted plus lambda function
def topKFrequent_Counter_sorted(words: List[str], k: int) -> List[str]:
    """ 
    Sort all the unique words in a list by (-freq, word) and slice the first k elements.
    
    Complexity Analysis:
    -------------------
    Time: O(U log(U)) due to sorting unique words
    Space: O(U) due to storing unique words
    
    Where do the unique words get stored?
    
    
    
    """
