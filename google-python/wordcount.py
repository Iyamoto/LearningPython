#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def get_word_dict(filename):
  assert type(filename)==str
  f = open(filename, 'rU')
  WordsDict = {}
  for line in f:
    line = line.strip().lower()
    words = line.split()
    for word in words:
      WordsDict[word] = WordsDict.get(word, 0) +1
  f.close()
  return WordsDict

def print_words(filename):
  WordsDict = get_word_dict(filename)
  for k, v in WordsDict.items(): print k, v
  return None

def get_count(wordtuple):
  return wordtuple[1]

def print_top(filename):
  WordsDict = get_word_dict(filename)
  SortedDict = sorted(WordsDict.items(), key=get_count, reverse=True)
  for item in SortedDict[:20]:
    print item[0], item[1]
  return None

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():

  filename = 'alice.txt'
  ##print_words(filename)
  print_top(filename)

if __name__ == '__main__':
  main()
