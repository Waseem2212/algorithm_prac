from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)  # Quick lookup for words
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])  # (current_word, step_count)

    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == endWord:
            return steps

        # Try changing each character in the current word
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i+1:]
                
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, steps + 1))

    return 0
