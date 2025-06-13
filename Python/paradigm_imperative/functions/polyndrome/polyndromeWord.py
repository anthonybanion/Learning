# Date: 21/08/2024
# Version: 1.0

"""
Statement:
Title: Polyndrome word
- Enter a word by keyboard
- print if the word is polyndrome or not 
"""

save_word1 = ""
save_word2 = ""

def print_word(word, save_word1):
    for i in range(len(word)):
        save_word1 += word[i]
    return save_word1


def print_word_inverted(word, save_word2):
    for i in range(len(word)-1, -1, -1):  
        save_word2 += word[i]
    return save_word2


entered_word = input("Enter a word: ")
if print_word(entered_word, save_word1) == print_word_inverted(entered_word, save_word2):
    print("The word is polyndrome")
else:
    print("the word is not palindrome")
