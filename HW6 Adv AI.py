#!/usr/bin/env python
# coding: utf-8

# Dassilva Petit<br> 
# Troy University<br>
# Homework6<br>
# Adv Artificial Inteligence<br> 
# 
# This week, you will be processing textual data in this File Download File. 
# 
# Remove all the punctuations and non-English words, then count the number of the rest of the words in the file
# Word counts. Extracting the most 20 frequent words from the file
# The source code file and the outputs of your programs are required to submit. 

# In[12]:


import re
from collections import Counter
import string


# In[13]:


# Function to remove punctuation and non-English words
def clean_text(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    
    # Remove non-English words 
    
    words = re.findall(r'\b[a-z]+\b', text)
    
    return words

# process the file and count words
def process_file(file_path): 
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Clean the text (remove punctuation and non-English words)
    words = clean_text(text)
    
    # Count the total number of words
    total_words = len(words)
    
    # Get the 20 most frequent words
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(20)
    
    return total_words, most_common_words

# Path to the text file
file_path = r'C:\Users\dassi\Downloads\Shakespeare.txt'  # Use raw string to avoid escape characters

# Process the file
total_words, most_common_words = process_file(file_path)

# Output results
print(f"Total number of words: {total_words}")
print("\nMost frequent 20 words:")
for word, count in most_common_words:
    print(f"{word}: {count}")


# In[ ]:




