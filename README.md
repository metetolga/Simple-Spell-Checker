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

## Minimum Edit Distance Algorithm
The minimum edit distance algorithm computes the smallest number of operations (insertions, deletions, and substitutions) required to transform one string into another. Below is an explanation of the implementation:

### Function: `min_edit_distance`
```python
import numpy as np

def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    m = len(source)
    n = len(target)

    D = np.zeros((m+1, n+1), dtype=int) 
    
    for row in range(1, m+1): 
        D[row, 0] = D[row-1, 0] + del_cost

    for col in range(1, n+1): 
        D[0, col] = D[0, col-1] + ins_cost
        
    for row in range(1, m+1): 
        for col in range(1, n+1):
            r_cost = rep_cost
            
            if source[row-1] == target[col-1]:
                r_cost = 0
                
            D[row, col] = min([
                D[row-1, col] + del_cost,  # Deletion
                D[row, col-1] + ins_cost,  # Insertion
                D[row-1, col-1] + r_cost  # Substitution
            ])
          
    med = D[m, n]
    return D, med
```

### Explanation

1. **Initialization**:
   - The matrix `D` is initialized with dimensions `(m+1) x (n+1)`, where `m` and `n` are the lengths of the `source` and `target` strings, respectively.
   - The first row and column are filled to account for converting the string to or from an empty string using only insertions or deletions.

2. **Filling the Matrix**:
   - The algorithm iterates through the matrix, row by row and column by column.
   - For each cell `(row, col)`, it calculates the minimum cost required to transform the substring `source[:row]` into `target[:col]`. This is done by considering:
     - **Deletion**: Removing a character from `source`.
     - **Insertion**: Adding a character to `source` to match `target`.
     - **Substitution**: Replacing a character in `source` with one from `target` (cost is 0 if the characters are the same).

3. **Result**:
   - The final cell `D[m, n]` contains the minimum edit distance.
   - The complete matrix `D` shows the cost of transforming prefixes of `source` into prefixes of `target`.

### Example
```python
source = "intention"
target = "execution"
D, med = min_edit_distance(source, target)
print("Minimum Edit Distance:", med)
```
**Output**:
```
Minimum Edit Distance: 8
```

The minimum edit distance between "intention" and "execution" is 8, as calculated by the algorithm.

