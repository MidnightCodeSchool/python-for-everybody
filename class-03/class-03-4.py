# pretty print
# from pprint import pprint
from rich import print
from rich.progress import track
from time import sleep

# word counter
paragraph = "The quick brown fox jumps over the lazy dog dog dog"
words = paragraph.split(" ")
word_count = {}
for word in track(words):
    sleep(1)
    print(word)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
