import collections
import threading
import time

def count_word(word, counter):
  # Get the current time
  start_time = time.time()

  # Count the frequency of the word in the counter object
  frequency = counter[word]
  
  # Print the frequency and the time taken to count it
  print(f'{word}: {frequency} ({time.time() - start_time:.20f} seconds)')

# Read the contents of the text file
with open('text.txt', 'r', encoding='utf-8') as f:
  text = f.read()

# Split the text into a list of words
words = text.split()

# Create a Counter object to count the frequencies of the words
counter = collections.Counter(words)

# Iterate over the range of 1 to 8
for i in range(1, 2):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('the', counter))
  t.start()

for i in range(1, 3):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('happy', counter))
  t.start()

for i in range(1, 4):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('people', counter))
  t.start()

for i in range(1, 5):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('that', counter))
  t.start()

for i in range(1, 6):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('this', counter))
  t.start()

for i in range(1, 7):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('and', counter))
  t.start()

for i in range(1, 8):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('at', counter))
  t.start()

for i in range(1, 9):
  # Start a new thread
  t = threading.Thread(target=count_word, args=('or', counter))
  t.start()
