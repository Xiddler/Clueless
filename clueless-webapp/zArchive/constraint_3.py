#!/usr/bin/python3
# encoding: utf-8

"""

  This is a module for Game 3 of Clueless - key letter is first AND last letter


"""

from collections import OrderedDict

# Sample form data by a user
# users_words = ['area', 'barb', 'citric', 'deed', 'eve', 'fluff', 'glugh', 'high', 'intermezzi', 'kick', 'legal', 'madam', 'nun', 'onto', 'pip', 'rear', 'sameness', 'that', 'whew', 'yearly']

# Empty dictionary
# tick = OrderedDict([('a', ''), ('b', ''), ('c', ''), ('d', ''), ('e', ''), ('f', ''), ('g', ''), ('h', ''), ('i', ''), ('j', ''), ('k', ''), ('l', ''), ('m', ''), ('n', ''), ('o', ''), ('p', ''), ('q', ''), ('r', ''), ('s', ''), ('t', ''), ('u', ''), ('v', ''), ('w', ''), ('x', ''), ('y', ''), ('z', '')])

tick = OrderedDict([('a', ''), ('b', ''), ('c', ''), ('d', ''), ('e', ''), ('f', ''), ('g', ''), ('h', ''), ('i', ''), ('k', ''), ('l', ''), ('m', ''), ('n', ''), ('o', ''), ('p', ''), ('r', ''), ('s', ''), ('t', ''), ('w', ''), ('y', '')])


# print("Original", tick)

def obeys_rule(users_words):
    """ method to check if user's input follows the constraint and provides feedback as tick or x """ 
    # for word in users_words: # users_words is the list of the user's input words
    for n in range(0, len(users_words)):
        if users_words[n] != '' and users_words[n][0] == users_words[n][-1]:
            # print("Acceptable")
            tick[users_words[n][0]] = '✅'
        elif users_words[n] != '':
                # print("Not acceptable")
                tick[users_words[n][0]] = '𐄂'
        else:
            print("PROBLEM 22")
    return tick

