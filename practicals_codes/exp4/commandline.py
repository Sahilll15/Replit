import sys

# Get command-line argument and join to form a sentence
sentence = ' '.join(sys.argv[1:])

# Display sentence and its length
print("Sentence:", sentence)
print("Length of sentence:", len(sentence))
