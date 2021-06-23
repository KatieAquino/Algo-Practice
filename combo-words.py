def get_combo_words(words):
    
    words_set = set(words)
    combo_words = []
    
    while words:
        word = words[-1]

        for i in range(1, len(word) - 1):
            front = word[:i]
            back = word[i:]
            
            if front in words_set and back in words_set:
                combo_words.append(word)

        del words[-1]

    return combo_words

results = get_combo_words(['pin', 'pine', 'apple', 'pineapple', 'pinapple'])
print(results)