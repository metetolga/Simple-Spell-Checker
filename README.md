# Basic Spell Checker

This repository implements a spell-checking algorithm based on the minimum edit distance. The main functionality is contained in `utils.py`, and the only required dependency besides Python is `numpy`.

## Overview of `utils.py` Functions

### `process_data`
Processes a given text file and extracts all words in lowercase. Words are identified using the regular expression `\w+`, which matches alphanumeric characters and underscores.

### `get_counter`
Generates a dictionary that counts the occurrences of each word in the processed data.

### `get_probs`
Calculates the probability of each word by dividing its frequency by the total number of words.

### `edit_one_letter`
Generates all possible variations of a word with one edit operation. The following operations are supported:

1. **Split**
   - Splits the word at every possible position into two parts: left and right.
   - Example:
     - **Word**: `play`
     - **Splits**: `[('', 'play'), ('p', 'lay'), ('pl', 'ay'), ('pla', 'y'), ('play', '')]`

2. **Delete**
   - Removes the first character of the right part of each split.
   - Example:
     - **Deletes**: `['lay', 'pay', 'ply', 'pla']`

3. **Switch**
   - Swaps the first two characters of the right part of each split.
   - Example:
     - **Switches**: `['lpay', 'paly', 'plya']`

4. **Replace**
   - Replaces the first character of the right part with every letter of the alphabet.
   - Example:
     - **Replaces**: `['alay', 'blay', 'clay', 'dlay', ...]`

5. **Insert**
   - Inserts every letter of the alphabet between the left and right parts of each split.
   - Example:
     - **Inserts**: `['aplay', 'bplay', 'cplay', ...]`

Combining these operations, `edit_one_letter` generates all possible one-edit variations of the input word.

### `edit_two_letters`
Generates all possible variations of a word with two edit operations by applying `edit_one_letter` twice.

## Choosing the Best Match
The algorithm evaluates all possible edited words and selects the one with the highest probability from the word frequency data.

This approach ensures that the most likely correction is suggested based on the input data.

