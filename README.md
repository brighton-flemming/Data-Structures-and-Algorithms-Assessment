# Data-Structures-and-Algorithms-Assessment

# Python Functions for Sentence Processing

This repository contains three Python functions for sentence processing:

1. `check_format(expression)`: This function checks if a given expression contains valid pairs of parentheses, square brackets, and curly braces. It returns `True` if the format is valid, and `False` otherwise.

2. `remove_duplicates(sequence)`: This function takes a sequence (list or tuple) and removes duplicate elements while preserving the order of elements. It returns a new sequence with duplicates removed.

3. `word_frequency(sentence)`: This function takes a sentence as input and returns a dictionary containing the frequency of each word in the sentence. Words are split based on whitespace, and common punctuation marks are removed for consistent counting.

## Usage

### Checking Format

```python
from format_checker import check_format

expression1 = "([]{})"
expression2 = "([)]"

result1 = check_format(expression1)  # Should return True
result2 = check_format(expression2)  # Should return False

print(result1)
print(result2)
Removing Duplicates
python
Copy code
from duplicate_remover import remove_duplicates

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
Word Frequency
python
Copy code
from word_counter import word_frequency

sentence = "This is a test sentence. This sentence is a test."

result = word_frequency(sentence)
print(result)

- Dependencies
No external libraries are required to use these functions.