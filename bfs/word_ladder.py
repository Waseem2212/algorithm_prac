from collections import deque

def wordLadderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)  # Convert wordList to set for fast lookup
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord, 1)])  # Queue with (current_word, steps)
    
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        
        # Try changing each letter in the word
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)  # Remove to prevent re-visiting
                    queue.append((new_word, steps + 1))
    
    return 0
