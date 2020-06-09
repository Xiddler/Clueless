#!/usr/bin/python3
# encoding: utf-8
# from collections import itertools

# Sample user input
# mid = ([('aword', 'area'), ('bword', 'barb'), ('cword', 'coslllee'), ('dword', 'did'), ('eword', ''), ('fword', ''), ('gword', ''), ('hword', ''), ('iword', ''), ('kword', ''), ('lword', ''), ('mword', ''), ('nword', ''), ('oword', ''), ('pword', ''), ('rword', ''), ('sword', ''), ('tword', ''), ('wword', ''), ('yword', ''), ('submit', 'Submit')])

def sanitized_input(alist):
    cleaned_input = []
    for elem in alist:
        elem = elem.lower()
        elem = elem.strip()
        cleaned_input.append(elem)
    return cleaned_input


# word_holder  = ['area', 'barb ', 'classic ', ' deed', 'eve', ' fluff ', ' gig ', ' high  ', '', ' kick   ', 'loyal ', ' madam', '', '', '', '', '', '', '', '']
# print(word_holder)
# print('_'*80)
# print(sanitized_input(word_holder))

