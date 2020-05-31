#!/usr/bin/python3
# encoding: utf-8

"""

  This is a module for Game 3 of Clueless - key letter is first AND last letter


"""

from string import ascii_lowercase as alfbet # lowercase letters of the alphabet built in
from collections import OrderedDict

# Sample form data by a user
# users_words = ['area', 'barb', 'citric', 'deed', 'eve', 'fluff', 'glugh', 'high', 'intermezzi', 'kick', 'legal', 'madam', 'nun', 'onto', 'pip', 'rear', 'sameness', 'that', 'whew', 'yearly']

# Empty dictionary
# tick = OrderedDict([('a', ''), ('b', ''), ('c', ''), ('d', ''), ('e', ''), ('f', ''), ('g', ''), ('h', ''), ('i', ''), ('j', ''), ('k', ''), ('l', ''), ('m', ''), ('n', ''), ('o', ''), ('p', ''), ('q', ''), ('r', ''), ('s', ''), ('t', ''), ('u', ''), ('v', ''), ('w', ''), ('x', ''), ('y', ''), ('z', '')])

tick = OrderedDict([('a', ''), ('b', ''), ('c', ''), ('d', ''), ('e', ''), ('f', ''), ('g', ''), ('h', ''), ('i', ''), ('k', ''), ('l', ''), ('m', ''), ('n', ''), ('o', ''), ('p', ''), ('r', ''), ('s', ''), ('t', ''), ('w', ''), ('y', '')])


# print("Original", tick)

def obeys_rule(users_words):
    """ method to make rule and filter user's words """
    # for word in users_words: # users_words is the list of the user's input words
    for n in range(0, len(users_words)):
        if users_words[n] != '' and users_words[n][0] == users_words[n][-1]:
            # print("Acceptable")
 # <span style='font-size:100px;'>&#10003;</span✓>
            # tick[users_words[n][0]] = '✓'
            tick[users_words[n][0]] = '✅'
            # print("Not acceptable")
        elif users_words[n] != '':
                # tick[users_words[n][0]] = 'N'
                tick[users_words[n][0]] = '𐄂'
        else:
            print("PROBLEM 22")
    return tick

# print(obeys_rule(users_words))


# if __name__ == "__main__":
    # obeys_rule(users_words)


