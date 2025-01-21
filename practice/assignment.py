def make_palindrome(word):
    n = len(word)
    # Start checking from the whole string down to its smallest part
    for i in range(n):
        # Check if the substring from i to the end is a palindrome
        if word[i:] == word[i:][::-1]:
            # Add the reversed part of the prefix (word[:i]) to the end 
            return word + word[:i][::-1]
        

phrase = "abcdc"
result = make_palindrome(phrase)
print(result)
