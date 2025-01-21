def shortest_string(word):
    # Check if the word is already a palindrome
    if word == word[::-1]:
        return word
    # Loop through string
    for i in range(len(word)):
        suffix = word[i:]
        reversed_suffix = suffix[::-1]
        # Check if suffix is a palindrome
        if suffix == reversed_suffix:
            # Add the reverse of the prefix(before the palindrome)
            prefix = word[:i]
            reversed_prefix = prefix[::-1]
            result = word + reversed_prefix
            return result
    

phrase = "abcdc"
reslt = shortest_string(phrase)
print(reslt)


