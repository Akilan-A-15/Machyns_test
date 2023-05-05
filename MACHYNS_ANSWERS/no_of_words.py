# 1) Write a program to read that file and count the number of times each word has appeared. Print the output.

from collections import Counter
filename = r"sample.txt"
with open(filename, encoding="UTF-8") as file:
    text = file.read()

word_counts = Counter(text.split())

for word, count in word_counts.items():
    print(f"{word}: {count}")
