from collections import defaultdict, Counter
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = Counter()

class AutocompleteSystem:
    """
    Approach:
    1. Use a Trie where each node keeps a Counter of all sentences passing through that node.
    2. When initializing, insert each sentence into the Trie with its frequency.
    3. For each character input:
        - If it's not '#', append to the current query and search the trie node matching the prefix.
        - Return the top 3 matching sentences sorted by:
            a. Highest frequency
            b. Lexicographical order (if frequencies are equal)
    4. On input '#', treat the current query as a completed sentence and update the Trie.

    Time Complexity:
    - insert(): O(L), where L = length of the sentence
    - input(c): 
        * O(P) for searching prefix of length P in Trie
        * O(M log 3) for pushing M matching sentences into a min-heap of size 3

    Space Complexity:
    - O(N * L), where N is number of unique sentences and L is average sentence length
    - Additional space for Counters stored at each TrieNode
    """
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_node = self.root
        self.current_input = ""
        for sentence, time in zip(sentences, times):
            self.insert(sentence, time)

    def insert(self, sentence: str, freq: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] += freq

    def search(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return {}
            node = node.children[char]
        return node.sentences

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.current_input, 1)
            self.current_input = ""
            self.current_node = self.root
            return []

        self.current_input += c
        matches = self.search(self.current_input)

        heap = []
        for sentence, freq in matches.items():
            heapq.heappush(heap, (-freq, sentence))
        result = []
        for _ in range(3):
            if heap:
                result.append(heapq.heappop(heap)[1])
        return result
