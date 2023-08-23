# your code goes here!

# How to determine if one word is an anagram for another?
#

A_LIST = ["python", "live", "sunny", "windy", "evil"]


class Anagram:
    """Takes in a word and checks against
    a list of words

    Args:
        word (_type_): str
        a_list (_type_): list
    """

    def __init__(self, word):
        self.word = word

    def match(self, a_list):
        matching_anagrams = []  # Store matching anagrams
        for a_word in a_list:
            if sorted(self.word) == sorted(a_word):
                matching_anagrams.append(a_word)

        return matching_anagrams


# user_input = input("Enter a word => ")
a = Anagram("nothpy")

matches = a.match(["python", "evil", "sunny", "windy", "vile"])
print(matches)
