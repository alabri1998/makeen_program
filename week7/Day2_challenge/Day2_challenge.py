# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:51:27 2023

@author: alabri1998
"""
def custom_sort(paragraph):
    articles = ['a', 'an', 'the']
    # Split the paragraph into individual words
    words = paragraph.split()
    # Remove leading and trailing punctuation marks from each word
    words = [word.strip('.,?!') for word in words]
    # Remove the articles from the list of words
    words = [word for word in words if word.lower() not in articles]
    # Join the words back into a paragraph
    cleaned_paragraph = ' '.join(words)
    return cleaned_paragraph


# Example usage
paragraphs = [
    "The quick brown fox jumps over a lazy dog.",
    "An apple a day keeps the doctor away.",
    "The cat and the hat.",
    "A dog is a man's best friend."
]

sorted_paragraphs = sorted(paragraphs, key=custom_sort)
print(sorted_paragraphs)